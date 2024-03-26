from django import forms

class RegistrationForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=False)
    email = forms.EmailField(required=False)
    contact_number = forms.CharField(required=False)
