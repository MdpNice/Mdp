from django.contrib import admin
from .models import Partner
from .models import PartnerKnown
from .models import PersonByPlace

admin.site.register(Partner)
admin.site.register(PartnerKnown)
admin.site.register(PersonByPlace)
