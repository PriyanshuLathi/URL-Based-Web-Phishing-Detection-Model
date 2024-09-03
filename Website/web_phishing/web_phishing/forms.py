from django import forms

class URLForm(forms.Form):
    url = forms.URLField(label='URL', max_length=200, required=True)
