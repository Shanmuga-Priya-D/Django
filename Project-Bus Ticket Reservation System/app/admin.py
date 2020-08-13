from django.contrib import admin
from .models import Contact,Fun,Bookings,BusInfo

# Register your models here.

admin.site.register(Contact)
admin.site.register(Bookings)
admin.site.register(Fun)
admin.site.register(BusInfo)