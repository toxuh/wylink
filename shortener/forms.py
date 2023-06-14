from django import forms

class URLInputForm(forms.Form):
    url = forms.URLField(label='', max_length=2000)
