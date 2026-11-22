from django import forms


class PostForm(forms.Form):
    author = forms.CharField(max_length=100)
    title = forms.CharField(max_length=200)
    content = forms.CharField(widget=forms.Textarea, max_length=2000)

class CommentForm(forms.Form):
    comment_author = forms.CharField(max_length=100)
    content = forms.CharField(widget=forms.Textarea, max_length=500)