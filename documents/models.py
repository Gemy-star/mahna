from django.db import models
from django.template.defaultfilters import slugify


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


class Location(models.Model):
    LOCATION_STATUS = (
        (1, 'ممتازة'),
        (2, 'جيده'),
        (3, 'سيئة')
    )
    status = models.SmallIntegerField(null=True, choices=LOCATION_STATUS)
    url = models.URLField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    ZONE_LEVEL = (
        (1, 'مرتفع'),
        (2, 'منخفض'),
    )
    zone_level = models.SmallIntegerField(null=True, choices=ZONE_LEVEL)
    FINISHING = (
        (1, 'دهانات'),
        (2, 'هيكل إنشائى'),
        (3, 'الأرضيات')
    )
    finishing = models.SmallIntegerField(null=True, choices=FINISHING)


def get_image_filename(instance, filename):
    title = instance.location.get_status_display()
    slug = slugify(title)
    return "location_images/%s-%s" % (slug, filename)


class LocationImages(models.Model):
    location = models.ForeignKey(Location, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=get_image_filename,
                              verbose_name='Image')



