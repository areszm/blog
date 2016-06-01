# -*- coding: utf-8 -*-
from django import forms
from django.forms.formsets import BaseFormSet
from django.core.exceptions import NON_FIELD_ERRORS
from django.forms import BaseModelFormSet
#from django.contrib.auth.models import User
#import os

from .models import Post, Comment, Document

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('grop_0', 'grop_1', 'grop_2', 'grop_3', 'grop_4', 'grop_5', 'title', 'text',)
        labels = {
            'title': ('Tytuł'),
            'Text': ('Tekst'),
            'grop_0': ('Główna'),
            'grop_1': ('Grupa 1'),
            'grop_2': ('Grupa 2'),
            'grop_3': ('Grupa 3'),
            'grop_4': ('Grupa 4'),
            'grop_5': ('Grupa 5'),
        }
        error_messages = {
            NON_FIELD_ERRORS: {
                'unique_together': "%(model_name)s's %(field_labels)s are not unique.",
            }
        }

class PostFormSet(BaseFormSet):
    def __init__(self, *args, **kwargs ):
        super(BaseFormSet, self).__init__(*args, **kwargs)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)

class CommentFormSet(BaseFormSet):
    def __init__(self, *args, **kwargs ):
        super(BaseFormSet, self).__init__(*args, **kwargs)

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('docfile', 'title',)
