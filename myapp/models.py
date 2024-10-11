from django.db import models

class Employee(models.Model):

    name=models.CharField(max_length=200)
    
    designation=models.CharField(max_length=200)

    department=models.CharField(max_length=200)

    salary=models.IntegerField()

    contact=models.IntegerField()

    address=models.CharField(max_length=200)