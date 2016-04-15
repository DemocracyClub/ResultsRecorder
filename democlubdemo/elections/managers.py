import requests

from django.db import models

class ElectionManager(models.Manager):
    def update_or_create_from_url(self, url, session=None):
        if session is None:
            session = requests.session()

        data = session.get(url).json()

        return self.update_or_create(
            ident=data['id'],
            defaults={
                'data': data,
            },
        )
