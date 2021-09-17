from django.db import models


class contact(models.Model):
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=100)
    email = models.EmailField(max_length=250)
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email


class Contacts(models.Model):
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=100)
    email = models.EmailField(max_length=250)
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
