from django import forms
from blog.models import Comments


class EmailSendForm(forms.Form):
    name =forms.CharField()
    email=forms.EmailField()
    to=forms.EmailField()
    comments=forms.CharField(widget=forms.Textarea, required=False)


class CommentsForm(forms.ModelForm):
    class Meta:
        model=Comments
        fields = ('name','email','body')