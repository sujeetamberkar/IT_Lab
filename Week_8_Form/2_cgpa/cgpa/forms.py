from django import forms
class InputData(forms.Form):
    name=forms.CharField(required=True)
    total=forms.IntegerField(required=True)
