# Generated by Django 4.0.2 on 2022-11-22 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0007_vendor_payment_account'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendor_payment',
            name='des',
            field=models.CharField(max_length=100, null=True),
        ),
    ]