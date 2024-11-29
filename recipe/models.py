from django.db import models
from django.contrib.auth.models import User


class Recipe(models.Model):
    name = models.CharField(max_length=255)
    ingredients = models.TextField()
    instructions = models.TextField()
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="recipes"
    )

    def __str__(self):
        return self.name


class RecipeBook(models.Model):
    name = models.CharField(max_length=255)
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="recipebooks"
    )
    shared_with = models.ManyToManyField(
        User, related_name="shared_recipebooks", blank=True
    )
    recipes = models.ManyToManyField(Recipe, through="RecipeBookRecipe")

    def __str__(self):
        return self.name


class RecipeBookRecipe(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    recipebook = models.ForeignKey(RecipeBook, on_delete=models.CASCADE)
