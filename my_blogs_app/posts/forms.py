from django import forms

class PostForm(forms.Form):
    title = forms.CharField(max_length=200)
    content = forms.CharField(widget=forms.Textarea, max_length=2000)

class CommentForm(forms.Form):
    content = forms.CharField(widget=forms.Textarea, max_length=500)