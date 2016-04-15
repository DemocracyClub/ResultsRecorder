import requests
import progressbar

from django.db import transaction
from django.core.management.base import BaseCommand

from ...models import Election, Post, Candidate

class Command(BaseCommand):
    BASE_URL = 'https://candidates.democracyclub.org.uk/api/v0.9/posts/'

    def handle(self, **options):
        url = self.BASE_URL

        self.session = requests.session()
        self.instances = {}

        pbar = progressbar.ProgressBar(widgets=(
            progressbar.SimpleProgress(),
            ' ',
            progressbar.Percentage(),
            ' ',
            progressbar.Bar(),
            ' ',
            progressbar.ETA(),
        ))

        while url is not None:
            self.stderr.write("Getting %s" % url)

            data = self.session.get(url).json()
            url = data['next']

            if pbar.maxval is None:
                pbar.maxval = data['count']
                pbar.start()

            for x in data['results']:
                self.process_post(x)
                pbar.update(pbar.currval + 1)

        pbar.finish()

    def update_or_create(self, model, data, **defaults):
        ident = data['id']

        try:
            return self.instances[model][ident]
        except KeyError:
            pass

        self.stderr.write("Syncing from %s" % data['url'])

        data = self.session.get(data['url']).json()
        defaults.setdefault('data', data)

        instance, _ = model.objects.update_or_create(
            ident=ident,
            defaults=defaults,
        )

        self.instances.setdefault(model, {})[ident] = instance

        return instance

    @transaction.atomic
    def process_post(self, data):
        for x in data['memberships']:
            if x['election'] is None:
                continue

            election = self.update_or_create(Election, x['election'])
            post = self.update_or_create(Post, x['post'], election=election)
            self.update_or_create(Candidate, x, post=post)
