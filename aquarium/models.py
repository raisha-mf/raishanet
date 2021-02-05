from django.db import models


class TankDimensions(models.Model):
    width = models.DecimalField(max_digits=10, decimal_places=1)
    depth = models.DecimalField(max_digits=10, decimal_places=1)
    height = models.DecimalField(max_digits=10, decimal_places=1)

    def __unicode__(self):
        return f'{self.width} x {self.depth} x {self.height}'

    def __str__(self):
        return f'{self.width} x {self.depth} x {self.height}'


class Flora(models.Model):
    name = models.CharField(max_length=256)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

class Fauna(models.Model):
    name = models.CharField(max_length=256)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

class Tank(models.Model):
    name = models.CharField(max_length=256)
    dimensions = models.ManyToManyField('aquarium.TankDimensions')
    flora = models.ManyToManyField('aquarium.Flora', null=True, blank=True)
    fauna = models.ManyToManyField('aquarium.Fauna', null=True, blank=True)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name