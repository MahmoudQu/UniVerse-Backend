# Generated by Django 5.1.3 on 2024-12-31 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0007_alter_jobpost_requirements_alter_jobpost_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='status',
            field=models.CharField(default='Pending', max_length=50),
        ),
    ]
