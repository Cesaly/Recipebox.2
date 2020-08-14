from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.models import User

from recipe_app.models import Recipe, Author
from recipe_app.forms import AddRecipeForm, AddAuthorForm, LoginForm
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
    return render(request, "author_detail.html",
                  {"author": author, "data": data})


@login_required
def addrecipe_view(request):
    if request.method == "POST":
        form = AddRecipeForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Recipe.objects.create(
                title=data.get('title'),
                author=request.user.author,
                description=data.get('description'),
                time_required=data.get('time_required'),
                instructions=data.get('instructions')
            )
            return HttpResponseRedirect(reverse("homepage"))

    form = AddRecipeForm()
    return render(request, "generic_form.html", {"form": form})


@login_required
@staff_member_required
def addauthor_view(request):
    if request.method == "POST":
        form = AddAuthorForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_user = User.objects.create_user(username=data.get("username"),
                                                password=data.get("password"))
            new_author = form.save(commit=False)
            new_author.user = new_user
            new_author.save()
        return HttpResponseRedirect(reverse("homepage"))

    form = AddAuthorForm()
    return render(request, "generic_form.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username=data.get('username'),
                                password=data.get('password'))
            if user:
                login(request, user)
                return HttpResponseRedirect(request.GET.get('next',
                                            reverse("homepage")))

    form = LoginForm()
    return render(request, "generic_form.html", {"form": form})



def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("homepage"))
