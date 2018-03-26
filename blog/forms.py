from django import forms

from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        #fields that end up in the form: user is already logged in and created_date is calculated
        fields = ('title', 'text',)
        