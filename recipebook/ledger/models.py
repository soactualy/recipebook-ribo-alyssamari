from datetime import datetime
from django.db import models
from django.urls import reverse
from users.models import Profile

# Create your models here.
class Ingredient(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('ledger:ingredient', args=[str(self.pk)])
    
    class Meta:
        verbose_name = 'ingredient'
        verbose_name_plural = 'ingredients'


class Recipe(models.Model):
    name = models.CharField(max_length=100)
    author = models.ForeignKey(Profile, null=True, on_delete=models.SET_NULL)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name}'
    
    def get_absolute_url(self):
        return reverse('ledger:recipe', args=[self.pk])
    
    class Meta:
        verbose_name = 'recipe'
        verbose_name_plural ='recipes'


class RecipeIngredient(models.Model):
    quantity = models.IntegerField()
    ingredient = models.ForeignKey(
        Ingredient,
        on_delete=models.CASCADE,
        null=False,
        related_name='recipe'
    )

    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        null=False,
        related_name='ingredients'
    )

    class Meta:
        verbose_name = 'recipe_ingredient'
        verbose_name_plural = 'recipe_ingredients'
    
class RecipeImage(models.Model):
    recipe_image = models.ImageField(upload_to='images/', null=False)
    description = models.CharField(max_length=255)

    image = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        null=False,
        related_name='images'
    )