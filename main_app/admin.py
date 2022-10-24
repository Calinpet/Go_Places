from django.contrib import admin
from .models import Place, Visit, Doing, Photo
# Register your models here.

admin.site.register(Place)

# register the new Visit Model
admin.site.register(Visit)
admin.site.register(Doing)
admin.site.register(Photo)

