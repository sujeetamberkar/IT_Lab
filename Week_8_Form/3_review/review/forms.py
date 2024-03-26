from django import forms

class VoteForm(forms.Form):
    CHOICES = [('good', 'Good'), ('satisfactory', 'Satisfactory'), ('bad', 'Bad')]
    vote = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
