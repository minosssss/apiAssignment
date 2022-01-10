from datetime import date
from django.db import models
from users.models import User
# Create your models here.


class Account(models.Model):
    # 자산구분
    # CASH = 'P001'
    # BANK = 'P002'
    # CREDIT = 'P003'
    # DEBIT = 'P004'

    ACCOUNT_CHOICES = (
        ('CASH', "현금"),
        ('BANK', "은행"),
        ('CREDIT', "신용카드"),
        ('DEBIT', "체크카드"),
    )
    type = models.CharField(max_length=10, choices=ACCOUNT_CHOICES)

    class Meta:
        db_table = 'account'

    def __str__(self):
        return self.group

class Category(models.Model):
    # 사용구분
    # MEAL = 'C001'
    # Transportation = 'C002'
    # ENTERTAINMENT = 'C003'
    # GROCERY = 'C004'
    # SHOPPING = 'C005'
    # HEALTH = 'C006'
    # EDUCATION = 'C007'
    # ETC = 'C008'

    CATEGORY_CHOICES = (
        ('MEAL', "식비"),
        ('TRANSPORTATION', "교통비"),
        ('ENTERTAINMENT', "문화생활"),
        ('GROCERY', "마트/편의점"),
        ('SHOPPING', "쇼핑"),
        ('HEALTH', "건강"),
        ('EDUCATION', "교육"),
        ('ETC', "기타"),
    )
    type = models.CharField(max_length=30, choices=CATEGORY_CHOICES)

    class Meta:
        db_table = 'category'

    def __str__(self):
        return self.type

class Payment(models.Model):
    # 자산세부
    name = models.CharField(max_length=20)
    group = models.ForeignKey(Account, related_name='payment_group', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='payment_user', on_delete=models.CASCADE)

    class Meta:
        db_table = 'payment'
        ordering = ['-user']

    def __str__(self):
        return f'{self.name}'


class Record(models.Model):

    INCM = 1
    EXPND = 2
    CLASSIFICATION_CHOICES = (
        (INCM, '수입'),
        (EXPND, '지출'),
        # ('ACTRSF', "이체"),
    )
    # Income or Expense
    classification = models.IntegerField(choices=CLASSIFICATION_CHOICES, default='지출', blank=False)
    # Dates
    date = models.DateField(default=date.today)
    # Relations
    category = models.ForeignKey(Category, related_name='record_category', on_delete=models.CASCADE)
    payment = models.ForeignKey(Payment, related_name='records_payment', on_delete=models.CASCADE)

    amout = models.IntegerField()
    note = models.CharField(max_length=100, blank=True)

    user = models.ForeignKey(User, related_name='record_user', on_delete=models.CASCADE)

    # On delete / True 활성화(유지), False 활성화(삭제)
    status = models.BooleanField(default=True)

    class Meta:
      db_table = 'record'

    def __str__(self):
        return f'{self.classification, self.date.__str__(), self.amout, self.status, self.payment}'