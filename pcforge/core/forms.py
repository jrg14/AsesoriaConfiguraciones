# forms.py

from django import forms

class ContactForm(forms.Form):
    first_name = forms.CharField(label='First name', max_length=100, required=True)
    last_name = forms.CharField(label='Last name', max_length=100, required=True)
    email = forms.EmailField(label='Email', max_length=100, required=True)
    country = forms.ChoiceField(label='Country', choices=[('US', 'US'), ('CA', 'CA'), ('EU', 'EU')], required=True)
    phone_number = forms.CharField(label='Phone number', max_length=15, required=True)
    message = forms.CharField(label='Message', widget=forms.Textarea, required=True)
    agree_to_policies = forms.BooleanField(label='Agree to policies', required=True)
