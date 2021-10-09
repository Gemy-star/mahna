from django.db import models


class ProfessionProof(models.Model):
    professionNumber = models.IntegerField(null=True, blank=True)
    date = models.DateField(null=True, blank=True)

    def __str__(self):
        return str(self.professionNumber)


class ConstructionFloor(models.Model):
    floorNumber = models.SmallIntegerField(null=True, blank=True)
    area = models.SmallIntegerField(null=True, blank=True)

    def __str__(self):
        return str(self.floorNumber)


class ConstructionLicense(models.Model):
    licenseNumber = models.IntegerField(primary_key=True)
    date = models.DateField(null=True, blank=True)
    buildingSurfaces = models.CharField(max_length=255, null=True, blank=True)
    usage = models.CharField(max_length=255, null=True, blank=True)
    floors = models.ManyToManyField(ConstructionFloor)

    def __str__(self):
        return str(self.licenseNumber)


class ProfessionDocument(models.Model):
    areaNumber = models.IntegerField(primary_key=True)
    plannedNumber = models.IntegerField(unique=True)
    district = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    apartmentNumber = models.IntegerField(null=True, blank=True)
    apartmentArea = models.IntegerField(null=True, blank=True)
    proof = models.ManyToManyField(ProfessionProof)

    def __str__(self):
        return str(self.areaNumber)


class Applicant(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    manager = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    fax = models.CharField(max_length=255, null=True, blank=True)
    recordCivilian = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name
