# Generated by Django 4.0.2 on 2022-11-22 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_company_des_customer_payment_des_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer_payment',
            name='vendor',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='vendor_payment',
            name='customer',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
