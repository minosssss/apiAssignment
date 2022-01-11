# Generated by Django 4.0.1 on 2022-01-10 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accountBook', '0002_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='payment',
            options={'ordering': ['-user']},
        ),
        migrations.AlterField(
            model_name='account',
            name='group',
            field=models.CharField(choices=[('CASH', '현금'), ('BANK', '은행'), ('CREDIT', '신용카드'), ('DEBIT', '체크카드')], max_length=10),
        ),
        migrations.AlterField(
            model_name='category',
            name='type',
            field=models.CharField(choices=[('MEAL', '식비'), ('TRANSPORTATION', '교통비'), ('ENTERTAINMENT', '문화생활'), ('GROCERY', '마트/편의점'), ('SHOPPING', '쇼핑'), ('HEALTH', '건강'), ('EDUCATION', '교육'), ('ETC', '기타')], max_length=30),
        ),
        migrations.AlterField(
            model_name='record',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]