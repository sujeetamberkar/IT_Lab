from django import forms

class CarForm(forms.Form):
    CHOICES = [
        ('volvo', 'Volvo'),
        ('saab', 'Saab'),
        ('mercedes', 'Mercedes'),
        ('audi', 'Audi'),
    ]
    cars = forms.ChoiceField(choices=CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    text = forms.CharField(label='Enter Model', widget=forms.TextInput(attrs={'class': 'form-control'}))

    def clean_text(self):
        text = self.cleaned_data['text']
        # Example custom validation: Ensure the model name is not just numbers
        if text.isdigit():
            raise forms.ValidationError("Model cannot be just numbers.")
        return text
