# Generated by Django 5.1.3 on 2024-12-18 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0004_company_address_company_image_company_phone_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='website_url',
        ),
        migrations.AddField(
            model_name='company',
            name='city',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='country',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='name',
            field=models.CharField(default='Unknown', max_length=20),
        ),
        migrations.AlterField(
            model_name='company',
            name='phone',
            field=models.CharField(blank=True, max_length=20, null=True, unique=True),
        ),
    ]
