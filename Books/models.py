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


class Button(models.Model):
    def __str__(self):
        return self.button1 + ":" + self.button2 + ":" + self.button3 + ":" + self.button4

    button1 = models.CharField(max_length=10)
    button2 = models.CharField(max_length=10)
    button3 = models.CharField(max_length=10)
    button4 = models.CharField(max_length=10)
