from django.db import models


class RollerCoaster(models.Model):
    name = models.CharField(max_length=60)
    year_opened = models.IntegerField(blank=True)
    park = models.ForeignKey('Park')
    active = models.BooleanField(default=True)
    manufacturer = models.ForeignKey('Manufacturer')

    class Meta:
        unique_together = ('name', 'park')

    def __repr__(self):
        return '<Rollercoaster: %s - %s>' % (self.name, self.park.name)

    def __str__(self):
        return self.name


class Park(models.Model):
    name = models.CharField(max_length=100)
    active = models.BooleanField(default=True)
    location = models.CharField(max_length=200)
    country = models.ForeignKey('Country')
    
    class Meta:
        unique_together = ('name', 'country')

    def __repr__(self):
        return '<Park: %s (%s)>' % (self.name, self.country.name)

    def __str__(self):
        return self.name


class Country(models.Model):
    name = models.CharField(max_length=30, unique=True)
    abbreviation = models.CharField(max_length=3)

    class Meta:
        verbose_name_plural = 'countries'

    def __repr__(self):
        return '<Country: %s>' % self.name

    def __str__(self):
        return self.name


class Manufacturer(models.Model):
    verbose_name = models.CharField(max_length=30, unique=True)
    common_name = models.CharField(max_length=30)

    def __repr__(self):
        return '<Manufacturer: %s>' % self.verbose_name 
    
    def __str__(self):
        return self.verbose_name
