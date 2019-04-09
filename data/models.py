from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Phone(models.Model):
    person = models.ForeignKey('Person', blank=True, null=True, on_delete=models.CASCADE)
    CELL = 'Cell'
    WORK = 'Work'
    HOME = 'Home'
    UNKNOWN = 'Unknown'
    PHONE_TYPE_CHOICES = (
        (CELL, 'Cell'),
        (WORK, 'Work'),
        (HOME, 'Home'),
        (UNKNOWN, 'Unknown')
    )
    phone_type = models.CharField(max_length=7, choices=PHONE_TYPE_CHOICES, default=UNKNOWN)
    phone_number = models.IntegerField()


class Contribution(models.Model):
    person = models.ForeignKey('Person', blank=True, null=True, on_delete=models.CASCADE)
    date = models.DateField()
    amount = models.IntegerField()
    CHECK = 'C'
    PAYPAL = 'P'
    ACTBLUE = 'A'
    SQUARE = 'S'
    CONTRIBUTION_METHOD_CHOICES = (
        (CHECK, 'Check'),
        (PAYPAL, 'Paypal'),
        (ACTBLUE, 'ActBlue'),
        (SQUARE, 'SQUARE')
    )
    contribution_method = models.CharField(max_length=1, choices=CONTRIBUTION_METHOD_CHOICES, default=CHECK)


class CallNote(models.Model):
    person = models.ForeignKey('Person', blank=True, null=True, on_delete=models.CASCADE)
    note = models.TextField()
    date = models.DateField(auto_now=True)


class Person(models.Model):
    committee = models.ForeignKey('Committee', blank=True, null=True, on_delete=models.CASCADE)
    first = models.CharField(max_length=30)
    last = models.CharField(max_length=30)
    business_name = models.CharField(max_length=50, blank=True)
    address = models.CharField(max_length=50, default='', blank=True)
    city = models.CharField(max_length=30, default='', blank=True)
    state = models.CharField(max_length=30, default='', blank=True)
    zip = models.IntegerField(null=True, blank=True, default=0)
    email = models.EmailField(default='', blank=True)

    def __str__(self):
        full_name = str(self.first) + ' ' + str(self.last)
        return full_name


class Committee(models.Model):
    users = models.ManyToManyField(User, related_name='users')
    name = models.CharField(max_length=75, default='')

    def __str__(self):
        return self.name
