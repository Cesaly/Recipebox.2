from django.shortcuts import render

from recipe_app.models import Recipe, Author
# Create your views here.


def index(request):
    data = Recipe.objects.all()
    return render(request, 'index.html', {'data': data})


def recipe_detail(request, recipe_id):
    recipe = Recipe.objects.filter(id=recipe_id).first()
    return render(request, "recipe_detail.html", {"recipe": recipe})


def author_detail(request, author_id):
    author = Author.objects.get(id=author_id)
    data = Recipe.objects.filter(author=author)
    return render(request, "author_detail.html", {"author": author},
                  {"data": data})
