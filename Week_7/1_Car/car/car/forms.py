from django import forms

class CarForm(forms.Form):
    CHOICES = [
        ('volvo', 'Volvo'),
        ('saab', 'Saab'),
        ('mercedes', 'Mercedes'),
        ('audi', 'Audi'),
    ]
    cars = forms.ChoiceField(choices=CHOICES)
    text = forms.CharField(label='Enter Model')
