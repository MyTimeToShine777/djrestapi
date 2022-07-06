from unicodedata import name
from django.db import models

# Create your models here.


class StudentData(models.Model):
    name = models.CharField(verbose_name="Student Name",
                            max_length=200, help_text="Batch 2022")
    age = models.PositiveIntegerField()
    contact_no = models.IntegerField()
    email = models.EmailField(max_length=200)
    qualification = models.CharField(
        max_length=300, verbose_name="Educational Qulification")
    skills = models.TextField(max_length=1000, verbose_name="IT Skills")
    address = models.TextField(max_length=10000, verbose_name="Native Address")
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
