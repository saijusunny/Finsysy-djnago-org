# Generated by Django 4.0.2 on 2022-11-23 06:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0013_expense_banking_reference_vendor_payment_ref_no_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer_payment',
            name='bnkid',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app1.accounts1'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='expense_banking',
            name='bnkid',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app1.accounts1'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vendor_payment',
            name='bnkid',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app1.accounts1'),
            preserve_default=False,
        ),
    ]