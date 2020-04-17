from django.db import models


# Create your models here.
class Book(models.Model):

    def __str__(self):
        return self.name + ": " + self.author

    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    type = models.CharField(max_length=100)


class Data(models.Model):
    def __str__(self):
        return self.data1 + ': ' + self.data2

    data1 = models.CharField(max_length=100)
    data2 = models.CharField(max_length=100, default=True)


class Buttons(models.Model):
    def __str__(self):
        return str(self.button1)

    button1 = models.BooleanField(default=False)
