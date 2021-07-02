from django import forms
from .models import Books, Comment
# from django.contrib.auth import get_user_model

inputAttrs = {
    'class': "form-control"
}


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            "text",
        ]
        widgets = {
          'text': forms.Textarea(attrs={'rows': 4, }),
        }


class AddBookForm(forms.ModelForm):
    class Meta:
        model =Books
        fields = [
            "title",
            "author",
            "book",
            "image"
        ]
