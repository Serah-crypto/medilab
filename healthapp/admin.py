from django.contrib import admin

# Register your models here.


from healthapp.models import *

admin.site.register(Patient)
admin.site.register(Myappointment)
