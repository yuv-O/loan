from django.db import models
from django.utils import timezone

class Borrower(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Loan(models.Model):
    borrower = models.ForeignKey(Borrower, on_delete=models.CASCADE)
    original_amount = models.DecimalField(max_digits=10, decimal_places=2)
    interest_rate = models.DecimalField(max_digits=5, decimal_places=2, default=8.0)  # 8% monthly
    start_date = models.DateField(default=timezone.now)
    current_balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def monthly_due(self):
        return (self.original_amount * self.interest_rate) / 100

    def __str__(self):
        return f"{self.borrower.name} - ₹{self.original_amount}"

class Payment(models.Model):
    loan = models.ForeignKey(Loan, on_delete=models.CASCADE)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
    date_paid = models.DateField(default=timezone.now)

    def __str__(self):
        return f"₹{self.amount_paid} on {self.date_paid}"
