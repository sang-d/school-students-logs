from django.db import models


class School(models.Model):
    name = models.CharField("Name", max_length=20)
    # students = []
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class Student(models.Model):
    sid = models.CharField("Student ID", max_length=20)
    first_name = models.CharField("First Name", max_length=20)
    last_name = models.CharField("Last Name", max_length=20)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
