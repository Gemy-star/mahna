from django.db import models


class ProfessionDocument(models.Model):
    areaNumber = models.IntegerField(primary_key=True)
    plannedNumber = models.IntegerField(unique=True)
    district = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    apartmentNumber = models.IntegerField(null=True, blank=True)
    apartmentArea = models.IntegerField(null=True, blank=True)
    professionNumber = models.IntegerField(null=True, blank=True)
    date = models.DateField(null=True, blank=True)

    def __str__(self):
        return str(self.areaNumber)
