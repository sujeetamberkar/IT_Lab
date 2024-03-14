from django import forms
class Data(forms.Form):
    CHOICES = [
        ('physics','Physics'),
        ('chemistry', 'Chemistry'),
        ('maths','Maths'),
    ]
    subject = forms.ChoiceField(choices=CHOICES)
    name = forms.CharField(label='name')
    rollnumber = forms.CharField(label='rollnumber')


