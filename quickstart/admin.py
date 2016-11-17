from django.contrib import admin

# Register your models here.
from .models import Orden, Line

admin.site.register(Orden)
admin.site.register(Line)