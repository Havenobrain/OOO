from django import forms
from .models import Article, UserResponse


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = [
            'author',
            'title',
            'text',
            'category',
            'upload',
            ]


class CommentForm(forms.ModelForm):
    class Meta:
        model = UserResponse
        fields = ['author',
                  'text',
                  ]