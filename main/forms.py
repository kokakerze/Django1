"""File creating PostForm from ModelForm."""
from django.forms import ModelForm, Textarea, TextInput

from .models import Post


class PostForm(ModelForm):
    """Set PostForm from ModelForm."""

    class Meta:
        """Meta class to sets fields and widgets to Form."""

        model = Post
        fields = ['title', 'description', 'content']
        widgets = {
            "title": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Название статьи"
            }),
            "description": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Описание статьи"
            }),
            "content": Textarea(attrs={
                "class": "form-control",
                "placeholder": "Содержимое"
            })
        }
