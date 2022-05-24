from django.db import models
#from author.models import Author

class Book(models.Model):
    title = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    publisher = models.CharField(max_length=255)
    language = models.CharField(max_length=255)
    numPages = models.IntegerField()
    #author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return {self.title}

class BookItem(models.Model):
    barCode = models.CharField(max_length=255)
    borrowed = models.DateField()
    dueDate = models.DateField()
    genre = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    publicationDate = models.CharField(max_length=255)

    def __str__(self):
        return {self.status}
