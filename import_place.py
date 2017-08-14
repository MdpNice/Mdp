import os, django, csv

os.environ['DJANGO_SETTINGS_MODULE'] = 'src.settings'

from django.conf import settings
django.setup()

from django.contrib.auth.models import User
from places.models import Place


User.objects.all()
me = User.objects.get(username='najeand')

# Import
# ------------------------------------
Place.objects.all().delete()

with open('place.csv', newline='') as csvfile:
    rows = csv.DictReader(csvfile, delimiter=';', quotechar='|')
    for row in rows:
        print ( row['plId'], ' - ', row['plTitle'] )
        Place.objects.create(user=me, title=row['plTitle'], where='I', lat=row['lat'], lng=row['lng'], observed=row['seen'], comment=row['plComment'])
# ------------------------------------
