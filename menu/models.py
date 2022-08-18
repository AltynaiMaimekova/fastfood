from django.db import models
from django.utils import timezone


class User(models.Model):
    email = models.EmailField(max_length=30, blank=True, unique=True, null=True)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.email


class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    card_number = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Worker(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    position = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(max_length=30)
    extra_price = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Food(models.Model):
    name = models.CharField(max_length=30)
    start_price = models.IntegerField(default=0)
    ingredients = models.ManyToManyField(Ingredient, through='Order')

    def __str__(self):
        return self.name


class Order(models.Model):
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE)
    order_date_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.food} with {self.ingredient} for {self.client}'






