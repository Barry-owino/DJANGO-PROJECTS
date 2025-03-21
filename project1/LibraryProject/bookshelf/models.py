from django.db import models

# Create your models here.

class Book (models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    isbn = models.CharField(max_length=225)
    publication_year = models.IntegerField()
    publisher = models.CharField(max_length=225, blank=True, null=True)
    edition = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.title
