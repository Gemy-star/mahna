# Generated by Django 3.0 on 2021-10-08 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0004_auto_20211008_1453'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicant',
            name='recordCivilian',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
