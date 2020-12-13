from django import forms
from .models import Article

class RawArticleForm(forms.ModelForm):
  class Meta:
        model = Article
        fields =[
            'title',
        ]