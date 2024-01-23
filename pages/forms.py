from django import forms

from pages.models import ContactModel


class ContactModelForms(forms.ModelForm):

    class Meta:
        model = ContactModel
        fields = ['name', 'email', 'subject', 'message']