# Generated by Django 5.1.3 on 2024-12-04 08:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('universities', '0002_department_delete_major'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='department',
            name='university',
        ),
    ]
