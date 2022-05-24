from django.db import models

class Author(models.Model):
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.firstName} {self.lastName}'
