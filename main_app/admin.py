from django.contrib import admin
from .models import Place, Visit
# Register your models here.

admin.site.register(Place)

# register the new Visit Model
admin.site.register(Visit)

