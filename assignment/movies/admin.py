from django.contrib import admin
from .models import *

admin.site.register(Movie)
admin.site.register(Theater)
admin.site.register(MovieSchedule)
admin.site.register(Booking)
