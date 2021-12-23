from django.db import models


class Gallery(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    photo = models.ImageField(upload_to="photos/gallery")
    time_create = models.DateField()


class Teacher(models.Model):
    fullname = models.CharField(max_length=100)
    about = models.TextField()
    photo = models.ImageField(upload_to="photos/teachers")


class Student(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.IntegerField()


class Message(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    mtext = models.TextField()
