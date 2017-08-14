import os, django, csv
from datetime import date

os.environ['DJANGO_SETTINGS_MODULE'] = 'src.settings'


from django.conf import settings
django.setup()

from django.contrib.auth.models import User
from partners.models import Partner


User.objects.all()
me = User.objects.get(username='najeand')

# Import
# ------------------------------------
Partner.objects.all().delete()

with open('partner.csv', newline='') as csvfile:
    rows = csv.DictReader(csvfile, delimiter=';', quotechar='|')
    for row in rows:
        print ( row['paFirstName'], row['paLastName'] )

        if row['paBirthday']:
            paBirthday = row['paBirthday']
        else:
            paBirthday = None

        #Partner.objects.create(user=me, firstname=row['paFirstName'], lastname=row['paLastName'], birthday=paBirthday)

# ------------------------------------
