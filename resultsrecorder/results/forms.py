from django import forms

from .models import ResultSet

class ResultSetForm(forms.ModelForm):
    class Meta:
        model = ResultSet
        fields = (
            'num_turnout_calculated',
            'num_turnout_reported',
            'num_spoilt_ballots',
        )

    def __init__(self, post, *args, **kwargs):
        self.post = post
        self.candidates = []

        super(ResultSetForm, self).__init__(*args, **kwargs)

        for x in post.candidates.all():
            name = 'candidate_%d' % x.pk

            self.fields[name] = forms.IntegerField()
            self.candidates.append((x, self[name]))

    def save(self, user):
        instance = super(ResultSetForm, self).save(commit=False)
        instance.user = user
        instance.post = self.post
        instance.save()

        winner = max((y.value(), x) for x, y in self.candidates)[1]

        for candidate, field in self.candidates:
            instance.candidate_results.create(
                candidate=candidate,
                is_winner=bool(candidate == winner),
                num_ballots_reported=field.value(),
            )

        return instance
