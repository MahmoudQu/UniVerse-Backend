# Generated by Django 5.1.3 on 2025-01-13 16:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('companies', '0002_company_is_accepted_company_proof_document'),
    ]

    operations = [
        migrations.CreateModel(
            name='PendingSignupRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='pending_request', to='companies.company')),
            ],
        ),
    ]
