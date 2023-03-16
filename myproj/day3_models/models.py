from django.db import models

# model for student
class Student(models.Model):
  fname = models.CharField(max_length=30)
  lname = models.CharField(max_length=30)
  
  class Meta:
    db_table = 'student'