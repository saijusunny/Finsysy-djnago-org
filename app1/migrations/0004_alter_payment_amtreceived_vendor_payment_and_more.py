# Generated by Django 4.0.2 on 2022-11-22 06:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_rename_status_vendor_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='amtreceived',
            field=models.FloatField(null=True),
        ),
        migrations.CreateModel(
            name='vendor_payment',
            fields=[
                ('vendorpymid', models.AutoField(primary_key=True, serialize=False, verbose_name='CUSTPYMID')),
                ('vendor', models.CharField(max_length=100)),
                ('customer', models.CharField(max_length=100)),
                ('amount_received', models.CharField(max_length=100)),
                ('date', models.DateField(null=True)),
                ('paid_through', models.CharField(max_length=100)),
                ('ref_no', models.CharField(max_length=100)),
                ('cid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.company')),
            ],
        ),
        migrations.CreateModel(
            name='customer_payment',
            fields=[
                ('customerpymid', models.AutoField(primary_key=True, serialize=False, verbose_name='CUSTPYMID')),
                ('customer', models.CharField(max_length=100)),
                ('vendor', models.CharField(max_length=100)),
                ('amount_received', models.CharField(max_length=100)),
                ('date', models.DateField(null=True)),
                ('received_through', models.CharField(max_length=100)),
                ('paym_ref_no', models.CharField(max_length=100)),
                ('bnk_ref_no', models.CharField(max_length=100)),
                ('file', models.FileField(default='default.jpg', upload_to='Customer')),
                ('cid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.company')),
            ],
        ),
    ]
