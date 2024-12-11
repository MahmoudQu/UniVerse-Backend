# Generated by Django 5.1.3 on 2024-12-11 14:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('educations', '0001_initial'),
        ('students', '0010_remove_student_skills_student_skills'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='education',
            name='students',
        ),
        migrations.AddField(
            model_name='education',
            name='student',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='educations', to='students.student'),
        ),
    ]