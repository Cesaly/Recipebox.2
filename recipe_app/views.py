from django.shortcuts import render, HttpResponseRedirect, reverse
from recipe_app.models import Recipe, Author
from recipe_app.forms import AddRecipeForm, EditRecipeForm, AddAuthorForm
# Create your views here.


def index(request):
    data = Recipe.objects.all()
    return render(request, 'index.html', {'data': data})


def recipe_detail(request, recipe_id):
    recipe = Recipe.objects.filter(id=recipe_id).first()
    favorites = request.user.author.favorites.all()
    return render(request, "recipe_detail.html", {"recipe": recipe, "favorites": favorites})


def author_detail(request, author_id):
    author = Author.objects.get(id=author_id)
    data = Recipe.objects.filter(author=author)
    favorites = request.user.author.favorites.all()
    return render(request, "author_detail.html",{"author": author, "data": data, "favorites": favorites})


def favorites_view(request, recipe_id):
    author = request.user.author
    selected_recipe = Recipe.objects.get(id=recipe_id)
    author.favorites.add(selected_recipe)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def addrecipe_view(request):
    if request.method == "POST":
        form = AddRecipeForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Recipe.objects.create(
                title=data.get('title'),
                author=data.get('author'),
                description=data.get('description'),
                time_required=data.get('time_required'),
                instructions=data.get('instructions')
            )
            return HttpResponseRedirect(reverse("homepage"))

    form = AddRecipeForm()
    return render(request, "generic_form.html", {"form": form})


def editrecipe_view(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    if request.method == "POST":
        form =AddRecipeForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            recipe.title = data['title']
            recipe.author = data['author']
            recipe.description = data['description']
            recipe.title = data['time_required']
            recipe.title = data['instructions']
            recipe.save()
        return HttpResponseRedirect(reverse('recipe_detail', args=[recipe.id]))
        
    data = {
       'title': recipe.title,
       'author': recipe.author,
       'description': recipe.description,
       'time_required': recipe.time_required,
       'instructions': recipe.instructions
    }
    form = AddRecipeForm(initial = data)
    return render(request, 'generic_form.html', {'form': form})


def addauthor_view(request):
    if request.method == "POST":
        form = AddAuthorForm(request.POST)
        form.save()
        return HttpResponseRedirect(reverse("homepage"))

    form = AddAuthorForm()
    return render(request, "generic_form.html", {"form": form})
