"""recipebox URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from recipe_app.views import index, recipe_detail, author_detail, addrecipe_view, addauthor_view, editrecipe_view, favorites_view

urlpatterns = [
    path('', index, name="homepage"),
    path('favorite/<int:recipe_id>/', favorites_view, name='favorite'),
    path('recipe/<int:recipe_id>/edit/', editrecipe_view),
    path('recipe/<int:recipe_id>/', recipe_detail, name='recipe_detail'),
    path('author/<int:author_id>/', author_detail),
    path('addrecipe/', addrecipe_view),
    path('addauthor/', addauthor_view),
    path('admin/', admin.site.urls),
]
