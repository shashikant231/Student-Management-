from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

PHONE_HELP_TEXT = "For e.g 1234-567-890, 1234-567890, etc."


# Create your models here.
GENDER_CHOICES = (
    ("Male", 'Male'),
    ("Female", 'Female'),

)

class School(models.Model):
    name = models.CharField(max_length=50)
    contact_no = PhoneNumberField("Phone Number", help_text=PHONE_HELP_TEXT)
    
    def __str__(self):
        return self.name

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    gender = models.CharField(max_length=15,choices=GENDER_CHOICES)
    school = models.ForeignKey(School,on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Book(models.Model):
    name = models.CharField(max_length=100)
    no_of_pages = models.PositiveIntegerField()
    student = models.ForeignKey(Student,on_delete=models.DO_NOTHING,related_name="student_book")

    def __str__(self):
        return self.name