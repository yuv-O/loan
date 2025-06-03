from django import forms
from .models import Payment

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['loan', 'amount_paid', 'date_paid']
        widgets = {
            'date_paid': forms.DateInput(attrs={'type': 'date'}),
        }
