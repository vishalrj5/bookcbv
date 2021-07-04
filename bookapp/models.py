from django.db import models

# Create your models here.

class BookModel(models.Model):
    book_name = models.CharField(max_length=120,unique=True)
    author = models.CharField(max_length=120)
    price = models.FloatField()
    pages = models.IntegerField()

    def __str__(self):
        return self.book_name
