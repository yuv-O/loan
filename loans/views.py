from django.shortcuts import render
from .models import Loan
from .utils import update_loan_balances
from django.shortcuts import redirect
from .forms import PaymentForm
from django.shortcuts import get_object_or_404

def loan_detail(request, loan_id):
    loan = get_object_or_404(Loan, id=loan_id)
    payments = loan.payment_set.order_by('-date_paid')  # latest first
    return render(request, 'loans/loan_detail.html', {'loan': loan, 'payments': payments})


def add_payment(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            payment = form.save()
            
            # Update loan balance
            loan = payment.loan
            loan.current_balance -= payment.amount_paid
            if loan.current_balance < 0:
                loan.current_balance = 0
            loan.save()

            return redirect('dashboard')
    else:
        form = PaymentForm()

    return render(request, 'loans/add_payment.html', {'form': form})


def dashboard(request):
    update_loan_balances()
    loans = Loan.objects.all()
    return render(request, 'loans/dashboard.html', {'loans': loans})
