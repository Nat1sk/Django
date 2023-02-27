from django.db import models

class Article(models.Model):
    title = models.CharField('Title', max_length=25)
    description = models.CharField('Description', max_length=255)
    owner = models.CharField('Owner', max_length=20)

    def __str__(self):
        return self.title
