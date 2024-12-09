from django.contrib import admin
from .models import Marcas, Automoviles, Clientes, Cotizacion
# Register your models here.

admin.site.register(Marcas)

class AutomovilesAdmin(admin.ModelAdmin):
    list_display = ['placa','color','clase','marca','modelo','capacidad','electrico']
    search_fields=['placa','color','clase','modelo']
admin.site.register(Automoviles, AutomovilesAdmin)

class ClientesAdmin(admin.ModelAdmin):
    list_display=['nombre','apellido','nit_ci','f_nacimiento']
admin.site.register(Clientes, ClientesAdmin)

class CotizacionAdmin(admin.ModelAdmin):
    list_display=['cliente','automovil','valor_asegurado','prima','tasa']
admin.site.register(Cotizacion,CotizacionAdmin)
