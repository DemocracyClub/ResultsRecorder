import datetime

from django.db import models

class ResultSet(models.Model):
    user = models.ForeignKey('auth.User', related_name='result_sets')

    post = models.ForeignKey(
        'elections.Post',
        related_name='result_sets',
    )

    num_turnout_calculated = models.IntegerField()
    num_turnout_reported = models.IntegerField()
    num_spoilt_ballots = models.IntegerField()

    is_final = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)

    created = models.DateTimeField(default=datetime.datetime.utcnow)

    class Meta:
        ordering = ('-created',)
        get_latest_by = 'created'

    def __unicode__(self):
        return u"pk=%d user=%r post=%r" % (
            self.pk,
            self.user,
            self.post,
        )

class CandidateResult(models.Model):
    result_set = models.ForeignKey(
        'results.ResultSet',
        related_name='candidate_results',
    )

    candidate = models.ForeignKey(
        'elections.Candidate',
        related_name='candidate_results',
    )

    num_ballots_reported = models.IntegerField()

    is_winner = models.BooleanField(default=False)

    created = models.DateTimeField(default=datetime.datetime.utcnow)

    class Meta:
        ordering = ('candidate',)
        get_latest_by = 'created'
        unique_together = (
            ('result_set', 'candidate'),
        )

    def __unicode__(self):
        return u"pk=%d title=%r" % (
            self.pk,
            self.title,
        )
