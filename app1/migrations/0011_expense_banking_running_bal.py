# Generated by Django 4.0.2 on 2022-11-22 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0010_expense_banking'),
    ]

    operations = [
        migrations.AddField(
            model_name='expense_banking',
            name='running_bal',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
