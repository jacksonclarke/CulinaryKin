from django.db import models
from django.contrib.auth import User
from django.db.models.signals import post_migrate
from django.dispatch import receiver

class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        # Setting the right plural name in the admin site.
        verbose_name_plural = 'Categories'
        # Setting the name field in alphabetical order
        ordering = ('name',)

    def __str__(self):
        return self.name
    
PREDEFINED_CATEGORIES = [
    "Appetizers",
    "Soups and Salads",
    "Main Dishes",
    "Breads",
    "Desserts",
    "Breakfast",
    "Holiday Favorites",
    "Snacks",
    "Sides",
    "Cookies",
    "Sauces",
    "Not Specified",
]

@receiver(post_migrate)
def check_categories(sender, **kwargs):
    # Check if Category is empty
    if Category.objects.count() == 0:
        # If empty, populate with predefined categories.
        for category_name in PREDEFINED_CATEGORIES:
            Category.objects.create(name=category_name)