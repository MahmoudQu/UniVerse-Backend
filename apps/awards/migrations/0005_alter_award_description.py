# Generated by Django 5.1.3 on 2024-12-13 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('awards', '0004_remove_award_end_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='award',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
