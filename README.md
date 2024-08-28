# EX 02 Django ORM Web Application

## Date: 26/09/2023

## AIM
To develop a Django application to store and retrieve data from a bank loan database using Object Relational Mapping(ORM).

## ENTITY RELATIONSHIP DIAGRAM
## DESIGN STEPS
## STEP 1:
Clone the problem from GitHub

## STEP 2:
Create a new app in Django project

## STEP 3:
Enter the code for admin.py and models.py

## STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM

## Admin.py

```
from django.contrib import admin
from .models import Customer, Loan, CustomerAdmin, LoanAdmin

admin.site.register(Customer, CustomerAdmin)
admin.site.register(Loan, LoanAdmin)
```

## Models.py

```
from django.db import models
from django.contrib import admin

class Customer(models.Model):
    customer_id = models.CharField(max_length=20, help_text="Customer ID")
    name = models.CharField(max_length=100)
    address = models.TextField()
    phone = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Loan(models.Model):
    loan_id = models.CharField(max_length=20, help_text="Loan ID")
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    interest_rate = models.DecimalField(max_digits=5, decimal_places=2)
    duration = models.IntegerField(help_text="Duration in months")
    start_date = models.DateField()

    def __str__(self):
        return f"{self.loan_id} - {self.customer.name}"

class LoanAdmin(admin.ModelAdmin):
    list_display = ('loan_id', 'customer', 'amount', 'interest_rate', 'duration', 'start_date')

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('customer_id', 'name', 'address', 'phone', 'email')
```

## OUTPUT
![Output](https://github.com/Darkwebnew/ORM/assets/143114486/57dd6b2a-dd9e-4083-a1d0-2bc16b2aa0d3)
## RESULT
Thus the program for creating a database using ORM hass been executed successfully
