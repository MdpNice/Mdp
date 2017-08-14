from django.db import models
from django.utils import timezone

from places.models import Place

class Partner(models.Model):
    user = models.ForeignKey('auth.User')
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200, null=True)
    birthday = models.DateField(null=True, blank=True)
    comment = models.TextField(null=True, blank=True)

    last_modif_date = models.DateTimeField(
            default = timezone.now, null=True)

    def publish(self):
        self.last_modif_date = timezone.now()
        self.save()

    def __str__(self):
        return '%s %s' % (self.firstname, self.lastname)


class PartnerKnown(models.Model):

    partner = models.ForeignKey(Partner, on_delete=models.CASCADE)

    SEEN_LIST = (
        ('B', 'B...'),
        ('A', 'A...'),
        ('P', 'P...'),
        ('M', 'M...'),
        ('F', 'F...'),
        ('P', 'P...'),
        ('V', 'V...'),
    )
    seen = models.CharField(
        max_length=1,
        choices=SEEN_LIST,
    )

class PersonByPlace(models.Model):

    partner = models.ForeignKey(Partner, related_name='personbyplace')
    place = models.ForeignKey(Place, related_name='personbyplace')

    DID_LIST = (
        ('B', 'B...'),
        ('F', 'F...'),
        ('P', 'P...'),
        ('E', 'E...'),
        ('C', 'C...'),
        ('S', 'S...'),
        ('F', 'F...'),
        ('W', 'SW...'),
    )

    seen = models.CharField(
        max_length=1,
        choices=DID_LIST,
        default='B',
    )
