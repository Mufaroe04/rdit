from django import forms
from .models import *
from ckeditor.widgets import CKEditorWidget
class UserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name', 'last_name','username', 'email','phone','avatar']
class BlogForm(forms.ModelForm):
     class Meta:
        model=Blog
        fields=['post','post_image']

class CommentForm(forms.ModelForm):
     class Meta:
        model=Comment
        exclude=['comment_by']
