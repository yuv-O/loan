from datetime import timedelta, date
from .models import Loan, Payment

def update_loan_balances():
    today = date.today()
    for loan in Loan.objects.all():
        last_payment = Payment.objects.filter(loan=loan).order_by('-date_paid').first()
        days_since_last_payment = (today - (last_payment.date_paid if last_payment else loan.start_date)).days

        if days_since_last_payment >= 30:
            missed_months = days_since_last_payment // 30
            monthly_due = loan.monthly_due()
            total_due = missed_months * monthly_due
            loan.current_balance += total_due
            loan.save()
