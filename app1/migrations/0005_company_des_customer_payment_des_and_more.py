# Generated by Django 4.0.2 on 2022-11-22 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_alter_payment_amtreceived_vendor_payment_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='des',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customer_payment',
            name='des',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='vendor_payment',
            name='ref_no',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
