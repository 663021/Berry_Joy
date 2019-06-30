from django.db import models

class Yogurt(models.Model):
    name = models.CharField(max_length = 120)
    text = models.TextField()
    price = models.IntegerField()
    mass = models.IntegerField() 

    def __str__(self):
        return self.name

class Stock(models.Model):
    name = models.CharField(max_length = 120)
    text = models.TextField()
    date_f = models.DateField()
    date_s = models.DateField()

    def __str__(self):
        return self.name

class Fruit(models.Model):
    name = models.CharField(max_length = 120)
    text = models.TextField()
    price = models.IntegerField()
    mass = models.IntegerField() 

    def __str__(self):
        return self.name

class Waffle(models.Model):
    name = models.CharField(max_length = 120)
    text = models.TextField()
    price = models.IntegerField()
    mass = models.IntegerField() 

    def __str__(self):
        return self.name

class Doughnut(models.Model):
    name = models.CharField(max_length = 120)
    text = models.TextField()
    price = models.IntegerField()
    mass = models.IntegerField() 

    def __str__(self):
        return self.name
