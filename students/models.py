from django.db import models

class Student(models.Model):
    roll_no = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    branch = models.CharField(max_length=100)
    college = models.CharField(max_length=100)
    semester = models.IntegerField()
    address = models.TextField()

    def __str__(self):
        return f"{self.roll_no} - {self.name}"

