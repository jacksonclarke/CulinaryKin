from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .forms import RecipeForm, RecipeBookForm, ShareRecipeBookForm
from .models import RecipeBook, Recipe, RecipeBookRecipe
from django.contrib.auth.models import User

@login_required
def share_recipe_book_link(request, recipe_book_id):
    recipe_book = get_object_or_404(RecipeBook, id=recipe_book_id)
    if request.user != recipe_book.owner:
        return redirect("recipe:user_recipe_books")

    if request.method == "POST":
        username = request.POST.get("username")
        try:
            user = User.objects.get(username=username)
            recipe_book.shared_with.add(user)
            share_link = request.build_absolute_uri(
                f"/recipe/view-recipe-book/{recipe_book_id}/"
            )
            return render(
                request,
                "recipe/share_recipe_book_link.html",
                {
                    "title": "Share Recipe Book",
                    "share_link": share_link,
                    "recipe_book": recipe_book,
                    "message": f"Successfully shared with {username}",
                },
            )
        except User.DoesNotExist:
            return render(
                request,
                "recipe/share_recipe_book_link.html",
                {
                    "title": "Share Recipe Book",
                    "recipe_book": recipe_book,
                    "error": "User does not exist",
                },
            )

    share_link = request.build_absolute_uri(
        f"/recipe/view-recipe-book/{recipe_book_id}/"
    )
    return render(
        request,
        "recipe/share_recipe_book_link.html",
        {
            "title": "Share Recipe Book",
            "share_link": share_link,
            "recipe_book": recipe_book,
        },
    )


@login_required
def create_recipe(request, recipe_book_id):
    recipe_book = get_object_or_404(RecipeBook, id=recipe_book_id)
    if (
        request.user != recipe_book.owner
        and request.user not in recipe_book.shared_with.all()
    ):
        return redirect("recipe:user_recipe_books")
    if request.method == "POST":
        form = RecipeForm(request.POST)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.created_by = request.user
            recipe.save()
            RecipeBookRecipe.objects.create(recipe=recipe, recipebook=recipe_book)
            return redirect("recipe:recipe_book_detail", recipe_book_id=recipe_book.id)
    else:
        form = RecipeForm()
    return render(
        request,
        "recipe/create_recipe.html",
        {
            "title": "Create Recipe",
            "form": form,
            "recipe_book": recipe_book,
        },
    )


@login_required
def user_recipe_books(request):
    owned_recipe_books = RecipeBook.objects.filter(owner=request.user)
    shared_recipe_books = RecipeBook.objects.filter(shared_with=request.user)
    return render(
        request,
        "recipe/user_recipe_books.html",
        {
            "title": "My Recipe Books",
            "owned_recipe_books": owned_recipe_books,
            "shared_recipe_books": shared_recipe_books,
        },
    )


@login_required
def recipe_book_detail(request, recipe_book_id):
    recipe_book = get_object_or_404(RecipeBook, id=recipe_book_id)
    recipes = recipe_book.recipes.all()
    return render(
        request,
        "recipe/recipe_book_detail.html",
        {
            "title": recipe_book.name,
            "recipe_book": recipe_book,
            "recipes": recipes,
        },
    )


@login_required
def share_recipe_book(request, recipe_book_id):
    recipe_book = get_object_or_404(RecipeBook, id=recipe_book_id, owner=request.user)
    if request.method == "POST":
        form = ShareRecipeBookForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data["user"]
            recipe_book.shared_with.add(user)
            return redirect("recipe:user_recipe_books")
    else:
        form = ShareRecipeBookForm()
    return render(
        request,
        "recipe/share_recipe_book.html",
        {
            "title": "Share Recipe Book",
            "form": form,
            "recipe_book": recipe_book,
        },
    )


@login_required
def view_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    return render(
        request,
        "recipe/view_recipe.html",
        {
            "title": recipe.name,
            "recipe": recipe,
            "user": request.user,
        },
    )


def view_recipe_book(request, recipe_book_id):
    recipe_book = get_object_or_404(RecipeBook, id=recipe_book_id)
    recipes = recipe_book.recipes.all()
    return render(
        request,
        "recipe/view_recipe_book.html",
        {
            "title": recipe_book.name,
            "recipe_book": recipe_book,
            "recipes": recipes,
        },
    )


@login_required
def create_recipe_book(request):
    if request.method == "POST":
        form = RecipeBookForm(request.POST)
        if form.is_valid():
            recipe_book = form.save(commit=False)
            recipe_book.owner = request.user
            recipe_book.save()
            return redirect("recipe:user_recipe_books")
    else:
        form = RecipeBookForm()
    return render(
        request,
        "recipe/create_recipe_book.html",
        {
            "title": "Create Recipe Book",
            "form": form,
        },
    )


@login_required
def delete_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    recipe_book = recipe.recipebook_set.first()
    if request.user == recipe.created_by or request.user == recipe_book.owner:
        recipe.delete()
        return redirect("recipe:recipe_book_detail", recipe_book_id=recipe_book.id)
    return redirect("recipe:view_recipe", recipe_id=recipe.id)
