from django import forms
from .models import Post, Comment
from django.forms.widgets import ClearableFileInput

class PostModelForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'rows':2}))
    class Meta:
        model = Post
        fields = ('content', 'image')

        widgets = {
            'image': forms.ClearableFileInput(attrs={'multiple': True, 'class': 'custom-file-input'}),
        }


class CommentModelForm(forms.ModelForm):
    body = forms.CharField(label='',
                            widget=forms.TextInput(attrs={'placeholder':'Add a comment...'}))
    class Meta:
        model = Comment
        fields = ('body',)

