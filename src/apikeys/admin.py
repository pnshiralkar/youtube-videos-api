from django.contrib import admin

# Register your models here.
from apikeys.models import ApiKey

admin.site.register(ApiKey)