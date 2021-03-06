# Generated by Django 3.0 on 2021-10-09 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0006_auto_20211008_1618'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConstructionFloor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('floorNumber', models.SmallIntegerField(blank=True, null=True)),
                ('area', models.SmallIntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ConstructionLicense',
            fields=[
                ('licenseNumber', models.IntegerField(primary_key=True, serialize=False)),
                ('date', models.DateField(blank=True, null=True)),
                ('buildingSurfaces', models.CharField(blank=True, max_length=255, null=True)),
                ('usage', models.CharField(blank=True, max_length=255, null=True)),
                ('floors', models.ManyToManyField(to='documents.ConstructionFloor')),
            ],
        ),
    ]
