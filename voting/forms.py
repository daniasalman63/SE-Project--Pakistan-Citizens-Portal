from django import forms

class NameForm(forms.Form):
    candidate = forms.CharField(label='candidate', max_length=100)