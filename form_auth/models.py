from django.db import models

# Article model to store blog articles in the database
class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.CharField(max_length=100)

def __str__(self):
    return self.title

