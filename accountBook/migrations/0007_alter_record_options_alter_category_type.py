# Generated by Django 4.0.1 on 2022-01-11 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accountBook', '0006_alter_record_amout'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='record',
            options={'ordering': ('-status', '-date')},
        ),
        migrations.AlterField(
            model_name='category',
            name='type',
            field=models.CharField(choices=[('식비', '식비'), ('교통비', '교통비'), ('문화생활', '문화생활'), ('마트/편의점', '마트/편의점'), ('쇼핑', '쇼핑'), ('건강', '건강'), ('교육', '교육'), ('기타', '기타')], max_length=30),
        ),
    ]
