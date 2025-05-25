# app/forms.py
from django import forms
from .models import PaymentNotice

class PaymentNoticeForm(forms.ModelForm):
    class Meta:
        model = PaymentNotice
        fields = ['amount', 'transfer_date', 'method', 'slip_image']
