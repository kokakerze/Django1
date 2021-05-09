"""File creating PostForm from ModelForm."""
from django import forms
from django.forms import ModelForm, Select, Textarea, TextInput
from main.models import Author, Comments, Post, Subscriber


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


class SubscriberForm(ModelForm):
    """Set PostForm from ModelForm."""

    author_id = forms.ModelChoiceField(
        queryset=Author.objects.all().order_by('name'),
        empty_label="Выберите автора",
        widget=forms.Select(
            attrs={"class": "form-control"}
        )
    )

    class Meta:
        """Meta class to sets fields and widgets to Form."""

        model = Subscriber
        fields = ['email_to', 'author_id']
        widgets = {
            "email_to": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Email подписчика "
            }

            ),
            # "author_id": Select(attrs={
            #     "class": "form-control",
            #     "placeholder": "Автор ID"
            # }),

        }

    def save(self, commit=True):
        """Manual save method for Subscriber."""
        print("Subscriber before save")
        # form.ModelForm.save(self,commit)
        sbr = super().save(commit=False)
        sbr.email_to = sbr.email_to.title()
        sbr.save()
        print("Subscriber after save")
        return sbr


class CommentsForm(ModelForm):
    """Set PostForm from ModelForm."""

    class Meta:
        """Meta class to sets fields and widgets to Form."""

        model = Comments
        fields = ['body', 'subs_id']
        widgets = {
            "body": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Ваш комментариий"
            }

            ),
            "subs_id": Select(attrs={
                "class": "form-control",
                "placeholder": "подписчика ID"
            }),

        }
