# Generated by Django 5.1.3 on 2024-12-25 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('educations', '0004_alter_education_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='education',
            name='present',
            field=models.BooleanField(default=False),
        ),
    ]