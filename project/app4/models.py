from django.db import models

# many to many relationship

class Genre(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name
    

class Book(models.Model):
    title = models.CharField(max_length=100)
    genre = models.ManyToManyField(Genre)

    def __str__(self):
        return self.title