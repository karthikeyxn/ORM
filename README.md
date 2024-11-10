# Ex-3: Django ORM Web Application

## DATE: 01-0-2024

## AIM
To develop a Django application to store and retrieve data from a bank loan database using Object Relational Mapping(ORM).

## ENTITY RELATIONSHIP DIAGRAM

![ORM(1)](https://github.com/user-attachments/assets/7303c463-2f53-4434-86e5-632330b17617)

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
from .models import Loan

@admin.register(Loan)
class LoanAdmin(admin.ModelAdmin):
    list_display = ('loan_id', 'customer_name', 'amount', 'interest_rate', 'duration_months', 'start_date')
    search_fields = ('customer_name', 'loan_id')
```

## Models.py

```
from django.db import models

class Loan(models.Model):
    loan_id = models.AutoField(primary_key=True)  # Auto incrementing primary key
    customer_name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    interest_rate = models.FloatField()
    duration_months = models.PositiveIntegerField()
    start_date = models.DateField()

    def __str__(self):
        return f"Loan ID: {self.loan_id} - {self.customer_name}"
```

## OUTPUT

![Screenshot 2024-09-01 211854](https://github.com/user-attachments/assets/ccd126ae-3b9a-4a0a-a479-dd468b5691c7)

![Screenshot 2024-09-01 211840](https://github.com/user-attachments/assets/9c729a8b-7069-4770-b1af-72e28a5203a1)

## RESULT
Thus the program for creating a database using ORM hass been executed successfully
