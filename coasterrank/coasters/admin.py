from django.contrib import admin
from models import RollerCoaster, Park, Country, Manufacturer


@admin.register(RollerCoaster)
class RollerCoasterAdmin(admin.ModelAdmin):
    list_display = ('name', 'park', 'year_opened', 'manufacturer')


admin.site.register(Park)
admin.site.register(Country)
admin.site.register(Manufacturer)
