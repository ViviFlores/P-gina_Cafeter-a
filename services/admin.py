from django.contrib import admin
from .models import Service

# Register your models here.

#clase para realizar la configuración extendida del administrador
class ServiceAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

# gestionar el modelo en el administrador
admin.site.register(Service, ServiceAdmin)
