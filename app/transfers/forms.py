import datetime

from django import forms
from django.conf import settings

from .models import Transfer

class TransferForm(forms.ModelForm):

    class Meta:
        model = Transfer
        fields = [
            'sender',
            'receiver',
            'amount'
        ]