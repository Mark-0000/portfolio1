from django import forms
from .models import Message


class ContactForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['first_name', 'last_name', 'email', 'message']
