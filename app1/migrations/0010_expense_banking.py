# Generated by Django 4.0.2 on 2022-11-22 10:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0009_customer_payment_running_bal_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='expense_banking',
            fields=[
                ('expenseid', models.AutoField(primary_key=True, serialize=False, verbose_name='exid')),
                ('date', models.DateField(null=True)),
                ('expenseaccount', models.CharField(max_length=100, null=True)),
                ('amount', models.IntegerField(null=True)),
                ('vendor', models.CharField(max_length=100, null=True)),
                ('customer', models.CharField(max_length=100, null=True)),
                ('tax', models.CharField(max_length=100, null=True)),
                ('reference', models.CharField(max_length=100, null=True)),
                ('note', models.CharField(max_length=255, null=True)),
                ('file', models.FileField(default='default.png', upload_to='purchase/expense')),
                ('cid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.company')),
            ],
        ),
    ]
