# Generated by Django 3.0 on 2021-10-08 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0003_applicant'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicant',
            name='fax',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
