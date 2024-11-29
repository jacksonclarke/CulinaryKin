from django import forms
from .models import RecipeBook, Recipe
from django.contrib.auth.models import User


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ["name", "ingredients", "instructions"]


class RecipeBookForm(forms.ModelForm):
    class Meta:
        model = RecipeBook
        fields = ["name"]


class ShareRecipeBookForm(forms.Form):
    user = forms.ModelChoiceField(queryset=User.objects.all(), label="Share with user")
