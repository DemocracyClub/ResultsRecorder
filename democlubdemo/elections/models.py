import datetime

from django.db import models
from django.contrib.postgres.fields import JSONField

from .managers import ElectionManager

class Election(models.Model):
    ident = models.CharField(max_length=255, unique=True)

    data = JSONField()

    created = models.DateTimeField(default=datetime.datetime.utcnow)

    objects = ElectionManager()

    class Meta:
        ordering = ('ident',)
        get_latest_by = 'created'

    def __unicode__(self):
        return u"ident=%r data=%r" % (
            self.ident,
            self.data,
        )

class Post(models.Model):
    election = models.ForeignKey(Election, related_name='posts')

    ident = models.CharField(max_length=255, unique=True)

    data = JSONField()

    created = models.DateTimeField(default=datetime.datetime.utcnow)

    class Meta:
        ordering = ('ident',)
        get_latest_by = 'created'

    def __unicode__(self):
        return u"ident=%r data=%r" % (
            self.ident,
            self.data,
        )

class Candidate(models.Model):
    post = models.ForeignKey(Post, related_name='candidates')

    ident = models.CharField(max_length=255, unique=True)

    data = JSONField()

    created = models.DateTimeField(default=datetime.datetime.utcnow)

    class Meta:
        ordering = ('ident',)
        get_latest_by = 'created'

    def __unicode__(self):
        return u"ident=%r data=%r" % (
            self.ident,
            self.data,
        )
