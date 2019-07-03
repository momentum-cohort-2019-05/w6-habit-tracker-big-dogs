from django import forms
from core.models import DailyRecord


class DailyRecordForm(forms.ModelForm):

    class Meta:
        model = DailyRecord
        fields = ['quantity']
