from django.contrib import admin
from .models import Album, Tour, BandHistory, BandMember
# Register your models here.

admin.site.register(Album)
admin.site.register(Tour)
admin.site.register(BandHistory)
admin.site.register(BandMember)