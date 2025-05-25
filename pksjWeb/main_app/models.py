from django.db import models
from django.contrib.auth.models import User


class Paymentlist(models.Model):
    METHOD_CHOICES = [
        ('promptpay', 'PromptPay'),
        ('bank', 'Bank Transfer'),
        ('other', 'Other'),
    ]
    STATUS_CHOICES = [
        ('overdue', 'ค้างชำระ'),
        ('Paid', 'ชำระแล้ว'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transfer_date = models.DateField()
    slip_image = models.ImageField(upload_to='payment_slips/')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='waiting')

    def __str__(self):
        return f'{self.user.username} - {self.amount} ({self.status})' 