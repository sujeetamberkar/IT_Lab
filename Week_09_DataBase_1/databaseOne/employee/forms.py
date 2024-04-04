from django import forms
from .models import Works
from .models import Lives

class WorksForm(forms.ModelForm):
    class Meta:
        model = Works
        fields = ['person_name', 'company_name', 'salary']

class CompanyForm(forms.Form):
    company_name = forms.CharField(label='Company Name', max_length=100)


class LivesForm(forms.ModelForm):
    class Meta:
        model = Lives
        fields = ['person_name', 'street', 'city']
