from django.db.models import Sum
from django.db import models
from django.contrib.auth.models import User
import datetime


# class Account(models.Model):
#    Name = models.CharField(max_length=20, unique=True)
#    balance =
#   def __str__(self):
#       return self.Name


class Transaction(models.Model):
    Type = (("Income", "Income"),
            ("Expense", "Expense"),
    )

    CategoryChoices = (
        (" ", " "),
        ('Debt Payment', 'Debt Payment'),
        ('Utilities', 'Utilities'),
        ('Food', 'Food'),
        ('Housing', 'Housing'),
        ("Transportation", "Transportation"),
        ('Insurance', 'Insurance'),
        ('Medical', 'Medical'),
        ('Personal Spending', 'Personal Spending'),
        ('Entertainment', 'Entertainment'),
        ('Miscellaneous', 'Miscellaneous'),
    )
    Amount = models.DecimalField(max_digits=20, decimal_places=2)
    Date = models.DateTimeField(default=datetime.datetime.now)
    Category = models.CharField(max_length=20, default=" ", choices=CategoryChoices)
    Type = models.CharField(max_length=10, choices=Type)
    Client = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    class Meta:
        ordering = ('Date',)


