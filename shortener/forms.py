from django import forms

class URLInputForm(forms.Form):
    url = forms.URLField(label='Original URL', max_length=2000)
