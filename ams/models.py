from django.db import models
from django.utils import timezone

class Section(models.Model):
    FACULTY = 'FA'
    DIVISION = 'DI'
    DEPARTMENT = 'DE'
    SCHOOL = 'SC'

    SECTION_CHOICES = (
        (FACULTY,'Faculty'),
        (DIVISION,'Division'),
        (SCHOOL,'School'),
        (DEPARTMENT,'Department')
    )

    name = models.CharField(max_length=64)
    section_type = models.CharField(max_length=2,choices=SECTION_CHOICES,default=DEPARTMENT)

class Location(models.Model):
    name = models.CharField(max_length=256)
    address = models.CharField(max_length=256)
    suburb = models.CharField(max_length=256)
    post = models.CharField(max_length=4)
    state = models.CharField(max_length=3)

class Incumbent(models.Model):

    def concat_name(self):
        if self.first_name != "" or self.first_name != None:
            if self.last_name != "" or self.last_name != None:
               return self.first_name + " " + self.last_name
            else:
               return ""
        else:
            return ""

    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    full_name = models.CharField(max_length=256,default=concat_name)
    email = models.EmailField()
    is_active = models.BooleanField(default=True)


class Role(models.Model):
    INCUMBENT_BASED = 'IN'
    LOCATION_BASED = 'SI'
    SECTION_BASED = 'SE'
    STOCK = 'ST'
    ASSIGNMENT_CHOICES = (
        (INCUMBENT_BASED,'Incumbent'),
        (LOCATION_BASED,'Site'),
        (SECTION_BASED,'Section'),
        (STOCK,'Stock')
    )

    title = models.CharField(max_length=64)
    assignment = models.CharField(max_length=2,choices=ASSIGNMENT_CHOICES,default=INCUMBENT_BASED)
    is_active = models.BooleanField(default=True)
    incumbent = models.ForeignKey(Incumbent)
    location = models.ForeignKey(Location)
    section = models.ForeignKey(Section)

class AssetType(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name

class Asset(models.Model):
    purchase_date = models.DateField()
    warranty_period = models.PositiveSmallIntegerField()
    value = models.DecimalField(max_digits=8, decimal_places=2)
    depreciation_rate = models.DecimalField(max_digits=2, decimal_places=2)
    registered = models.DateTimeField(auto_now_add=True, editable=False)
    is_active = models.BooleanField(default=True)
    asset_type = models.ForeignKey(AssetType)
    role = models.ForeignKey(Role)

    def years_owned(self):
        difference = timezone.now() - self.purchase_date
        return difference.days / 365

    def depreciated_value(self):
        return self.value * ( ( 1 - self.depreciation_rate ) ** self.years_owned() )

class AssetExtendedTemplate(models.Model):
    field_name = models.CharField(max_length=64)
    asset_type = models.ForeignKey(AssetType)


class AssetExtendedFields(models.Model):
    key = models.CharField(max_length=64)
    value = models.CharField(max_length=64)
    regex = models.CharField(max_length=128)
    asset = models.ForeignKey(Asset)

class AssetLog(models.Model):
    comment = models.TextField()
    posted = models.DateTimeField(auto_now_add=True)
    asset = models.ForeignKey(Asset)

class RoleLog(models.Model):
    comment = models.TextField()
    posted = models.DateTimeField(auto_now_add=True)
    role = models.ForeignKey(Role)

