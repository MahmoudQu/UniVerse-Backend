# Generated by Django 5.1.3 on 2024-12-19 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resumes', '0002_alter_resume_file_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='resume',
            name='file_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='resume',
            name='file_name',
            field=models.CharField(max_length=50),
        ),
    ]
