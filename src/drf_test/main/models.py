from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    date_of_death = models.DateField(null=True, blank=True)
    biography = models.TextField()
    books = models.ManyToManyField('Book', related_name='authors')

    def __str__(self):
        return f'{self.name} {self.last_name}'


class Book(models.Model):
    title = models.CharField(max_length=255)
    genre = models.CharField(max_length=100)
    description = models.TextField()
    pub_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title
