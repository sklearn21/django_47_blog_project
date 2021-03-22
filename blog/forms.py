from django import forms


class EmailSendForm(forms.Form):
    name =forms.CharField()
    email=forms.EmailField()
    to=forms.EmailField()
    comments=forms.CharField(widget=forms.Textarea, required=False)
