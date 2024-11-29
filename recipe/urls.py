from django.urls import path
from . import views

app_name = "recipe"

urlpatterns = [
    path("create/<int:recipe_book_id>/", views.create_recipe, name="create_recipe"),
    path("my-recipe-books/", views.user_recipe_books, name="user_recipe_books"),
    path("create-recipe-book/", views.create_recipe_book, name="create_recipe_book"),
    path(
        "share-recipe-book/<int:recipe_book_id>/",
        views.share_recipe_book,
        name="share_recipe_book",
    ),
    path(
        "share-recipe-book-link/<int:recipe_book_id>/",
        views.share_recipe_book_link,
        name="share_recipe_book_link",
    ),
    path("view-recipe/<int:recipe_id>/", views.view_recipe, name="view_recipe"),
    path(
        "view-recipe-book/<int:recipe_book_id>/",
        views.view_recipe_book,
        name="view_recipe_book",
    ),
    path(
        "recipe-book-detail/<int:recipe_book_id>/",
        views.recipe_book_detail,
        name="recipe_book_detail",
    ),
    path("delete-recipe/<int:recipe_id>/", views.delete_recipe, name="delete_recipe"),
    # Add other URL patterns here
]
