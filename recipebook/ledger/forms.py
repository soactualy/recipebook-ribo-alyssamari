from django import forms
from .models import Recipe, RecipeImage


class RecipeForm(forms.ModelForm):
    name = forms.CharField(label='Recipe Name', max_length=100)

    class Meta:
        model = Recipe
        fields = "__all__"
        verbose_name = 'recipe_RecipeForm'
        verbose_name_plural = 'recipe_RecipeForms'


class RecipeImageForm(forms.ModelForm):
    class Meta:
        model = RecipeImage
        fields = ('image', 'description')
