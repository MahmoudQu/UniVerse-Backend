# Generated by Django 5.1.3 on 2024-11-25 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_refreshtoken'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='is_logged_in',
            field=models.BooleanField(default=False),
        ),
    ]
