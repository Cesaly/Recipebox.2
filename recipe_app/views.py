from django.shortcuts import render

from recipe_app.models import Recipe
# Create your views here.


def index(request):
    data = Recipe.objects.all()
    return render(request, 'index.html', {'data': data})


def recipe_detail(request, recipe_id):
    return render(request, "recipe_detail.html", {"recipe_id": recipe_id})
