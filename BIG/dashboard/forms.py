from django import forms
from .models import *

# class PostForm(forms.Form):
#     title = forms.CharField(label='제목')
#     content = forms.CharField(label='내용', widget=forms.Textarea)

class NoticeModelForm(forms.ModelForm):
    class Meta:
        model = Notice
        fields = ['title', 'content']

class QnAModelForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['title', 'writer', 'content']
