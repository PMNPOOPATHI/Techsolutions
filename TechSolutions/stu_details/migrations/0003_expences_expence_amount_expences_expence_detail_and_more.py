# Generated by Django 5.1.4 on 2025-02-27 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stu_details', '0002_accounts_expences'),
    ]

    operations = [
        migrations.AddField(
            model_name='expences',
            name='Expence_Amount',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='expences',
            name='Expence_detail',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='expences',
            name='c_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='expences',
            name='date',
            field=models.DateField(null=True),
        ),
    ]
