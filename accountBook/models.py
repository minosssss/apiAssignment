from datetime import date
from django.db import models
from users.models import User
# Create your models here.


class Payment(models.Model): # 지불방식
    """ Custom User Model """
    CASH = 10
    BANK = 11
    CREDIT = 12
    DEBIT = 13

    PAYMENT_CHOICES = (
        (CASH, "Cash"),
        (CREDIT, "Credit Card"),
        (DEBIT, "Debit Card"),
        (BANK, "Bank"),
    )
    type = models.IntegerField(choices=PAYMENT_CHOICES)
    name = models.CharField(max_length=20)

    class Meta:
        db_table = 'payment'

    def __str__(self):
        return self.name

class Category(models.Model): # 사용 구분
    classification = models.BooleanField(default=False) #True 수입, False 지출
    name = models.CharField(max_length=20)

    class Meta:
        db_table = 'category'

    def __str__(self):
        return self.name

class Record(models.Model):
    memo = models.CharField(max_length=100, blank=True)
    amount = models.IntegerField()

    # Relations
    category = models.ForeignKey(Category, related_name='records', on_delete=models.CASCADE)
    payment = models.ForeignKey(Payment, related_name='records', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='records', on_delete=models.CASCADE)

    # Dates
    date = models.DateField(default=date.today)

    class Meta:
      db_table = 'record'

    def __str__(self):
        return self.date