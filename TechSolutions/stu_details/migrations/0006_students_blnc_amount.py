# Generated by Django 5.1.4 on 2025-03-14 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stu_details', '0005_billing_balance_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='students',
            name='blnc_amount',
            field=models.IntegerField(null=True),
        ),
    ]
