from django import forms
from .models import MessageModel, FlightModel


class MessageModelForm(forms.ModelForm):
    class Meta:
        model = MessageModel
        fields = ['email', 'text']
