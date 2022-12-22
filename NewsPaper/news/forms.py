from django import forms
from django.core.exceptions import ValidationError

from .models import Post


class PostEditForm(forms.ModelForm):
    content = forms.CharField(min_length=10)

    class Meta:
        model = Post
        fields = [
            'header',
            'content',
            'subhub',
            'restriction',
        ]

    def clean(self):
        cleaned_data = super().clean()
        header = cleaned_data.get('header')
        content = cleaned_data.get('content')

        if header == content:
            raise ValidationError(
                "Content cannot be identical to header"
            )

        return cleaned_data


class PostCreateForm(forms.ModelForm):
    content = forms.CharField(min_length=10)

    class Meta:
        model = Post
        fields = [
            'author',
            'header',
            'content',
            'subhub',
            'restriction',
        ]

    def clean(self):
        cleaned_data = super().clean()
        header = cleaned_data.get('header')
        content = cleaned_data.get('content')

        if header == content:
            raise ValidationError(
                "Content cannot be identical to header"
            )

        return cleaned_data
