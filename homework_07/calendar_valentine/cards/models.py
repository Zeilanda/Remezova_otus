from django.db import models


class Card(models.Model):
    name = models.CharField(max_length=64)
    title = models.CharField(max_length=64)
    body = models.TextField()

    def __str__(self):
        return f'{self.name}'


class Master(models.Model):
    name = models.CharField(max_length=64)
    body = models.TextField()

    def __str__(self):
        return self.name, self.body
