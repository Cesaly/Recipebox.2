from django.db import models


# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=30)
    bio = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    title = models.CharField(max_length=30)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    description = models.TextField()
    time_required = models.CharField(max_length=30)
    instructions = models.TextField(max_length=60)

    def __str__(self):
        return self.title
