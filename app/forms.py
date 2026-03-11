from django import forms


class JsonUploadForm(forms.Form):
    file = forms.FileField(label='JSON файл')