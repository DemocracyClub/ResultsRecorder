import datetime

from django import forms

from resultsrecorder.results.models import ResultSet

class ConfirmForm(forms.ModelForm):
    class Meta:
        model = ResultSet
        fields = (
        )

    def save(self, request):
        instance = super(ConfirmForm, self).save(commit=False)
        instance.updated = datetime.datetime.utcnow()
        instance.confirmed_by = request.user
        instance.save()

        return instance

    def clean(self):
        qs = self.instance.post.result_sets.filter(confirmed_by__isnull=False)

        if qs.exists():
            raise forms.ValidationError(
                "A result set for this post already exists."
            )

        return self.cleaned_data
