# Generated by Django 5.1.3 on 2025-01-13 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admins', '0005_alter_admin_password'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='admin',
            name='last_login',
        ),
        migrations.AlterField(
            model_name='admin',
            name='is_admin',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='admin',
            name='password',
            field=models.CharField(max_length=255),
        ),
    ]
