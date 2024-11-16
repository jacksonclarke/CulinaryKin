from django.db import models
from django.contrib.auth.models import User
# from django.db.models.signals import post_migrate
# from django.dispatch import receiver


class Category(models.Model):
    name = models.CharField(max_length=255)


class Recipe(models.Model):
    title = models.CharField(max_length=255)
    ingredients = models.TextField()
    instructions = models.TextField()
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="recipes"
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="recipes",
    )


class RecipeBook(models.Model):
    name = models.CharField(max_length=255)
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="recipebooks"
    )
    shared_with = models.ManyToManyField(
        User, related_name="shared_recipebooks", blank=True
    )
    recipes = models.ManyToManyField(Recipe, through="RecipeBookRecipe")


class RecipeBookRecipe(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    recipebook = models.ForeignKey(RecipeBook, on_delete=models.CASCADE)
    added_by = models.ForeignKey(User, on_delete=models.CASCADE)
