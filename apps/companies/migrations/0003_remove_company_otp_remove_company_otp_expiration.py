# Generated by Django 5.1.3 on 2024-11-20 19:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0002_company_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='otp',
        ),
        migrations.RemoveField(
            model_name='company',
            name='otp_expiration',
        ),
    ]
