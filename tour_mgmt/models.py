from django.db import models
from django.contrib.gis.db import models as geo_models

from autoslug import AutoSlugField
from image_gallery.models import Gallery

class Tour(models.Model):
    name = models.CharField(max_length=120)
    slug = AutoSlugField(populate_from='name', unique_with=['name'])
    desc = models.TextField()
    ongoing = models.BooleanField(default=False)

    gallery = models.ForeignKey(Gallery, null=True, blank=True)

    def __unicode__(self):
        return self.name

class Stage(geo_models.Model):
    tour = models.ForeignKey(Tour, related_name="stages")
    name = models.CharField(max_length=120)
    place = models.CharField(max_length=120, null=True, blank=True)
    desc = models.TextField()
    order = models.PositiveSmallIntegerField()

    begin_date = models.DateField()
    duration = models.PositiveSmallIntegerField(default=1)

    point = geo_models.PointField()


    def __unicode__(self):
        return "%s #%s %s" % (self.order, self.tour.name, self.name)

    class Meta:
        ordering = ['tour__name', 'order']
