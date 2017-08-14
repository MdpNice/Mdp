from django.db import models
from django.utils import timezone
from django import forms

class Place(models.Model):
    user = models.ForeignKey('auth.User')
    title = models.CharField(max_length=250)
    WHERE_LIST = (
        ('I', 'In'),
        ('O', 'Out'),
    )
    where = models.CharField(max_length=1, choices=WHERE_LIST, default='O')
    lat = models.DecimalField(max_digits=11, decimal_places=9)
    lng = models.DecimalField(max_digits=11, decimal_places=9)
    observed = models.BooleanField()
    share = models.BooleanField(default=True)
    comment = models.TextField(null=True, blank=True)

    last_modif_date = models.DateTimeField(
            default=timezone.now, null=True)

    def publish(self):
        self.last_modif_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
    
