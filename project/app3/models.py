from django.db import models

# one-to one

class User(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    biography = models.TextField()

    