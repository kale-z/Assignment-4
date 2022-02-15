from __future__ import unicode_literals
from django.db import models



class Teacher(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    office = models.CharField(max_length=25)
    phone = models.CharField(max_length=13)
    email = models.EmailField()


class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()


class Course(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=10)
    classroom = models.CharField(max_length=25)
    time = models.CharField(max_length=100)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    students = models.ManyToManyField(Student)