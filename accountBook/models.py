from datetime import date
from django.db import models
from users.models import User
from choice import *
# Create your models here.


class Account(models.Model): # 지불방식
    """ Custom User Model """
    
    group = models.CharField(choices=ACCOUNT_CHOICES)
    name = models.CharField(max_length=20)
    user = models.ForeignKey(User, related_name='account', on_delete=models.CASCADE)

    class Meta:
        db_table = 'account'

    def __str__(self):
        return self.name

class Category(models.Model): # 사용 구분

    type = models.CharField(choices=CATEGORY_CHOICES)
    
    class Meta:
        db_table = 'category'

    def __str__(self):
        return self.name

class Record(models.Model):
    # Income or Expense
    classification = models.BooleanField(default=False) #True 수입, False 지출
    # Dates
    date = models.DateField(default=date.today)
    note = models.CharField(max_length=100, blank=True)
    amout = models.IntegerField()

    # Relations
    category = models.ForeignKey(Category, related_name='records', on_delete=models.CASCADE)
    account = models.ForeignKey(Payment, related_name='records', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='records', on_delete=models.CASCADE)
    

    class Meta:
      db_table = 'record'

    def __str__(self):
        return self.date