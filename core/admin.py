from django.contrib import admin
from core.models import Doctor

admin.site.site_header = "App Medica"
admin.site.site_title = "App Medica Admin"
admin.site.register(Doctor)