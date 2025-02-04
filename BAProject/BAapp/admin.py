from django.contrib import admin
from .models import *
# Register your models here.

class ItemPropuestaInline(admin.TabularInline):
    model = ItemPropuesta
    extra = 1

class PropuestaAdmin(admin.ModelAdmin):
    inlines = (ItemPropuestaInline,)

class ArticuloAdmin(admin.ModelAdmin):
    inlines = (ItemPropuestaInline,)

class FacturaAdmin(admin.ModelAdmin):
    list_display  = ('fecha_emision','documento')

admin.site.register(Comprador)
admin.site.register(Logistica)
admin.site.register(Administrador)
admin.site.register(Proveedor)
admin.site.register(Articulo, ArticuloAdmin)
admin.site.register(Presupuesto)
admin.site.register(Propuesta, PropuestaAdmin)
admin.site.register(Vendedor)
admin.site.register(Empresa)
admin.site.register(Retencion)
admin.site.register(Domicilio)
admin.site.register(DomicilioPostal)
admin.site.register(Telefono)
admin.site.register(Gerente)
admin.site.register(ItemPropuesta)
admin.site.register(Financiacion)
admin.site.register(Negocio)
admin.site.register(Persona)
admin.site.register(TipoPago)
admin.site.register(Notificacion)
admin.site.register(Factura, FacturaAdmin)
admin.site.register(Remito)
admin.site.register(OrdenDeCompra)
admin.site.register(OrdenDePago)
admin.site.register(ContansiaRentencion)
admin.site.register(Recibo)
admin.site.register(Cheque)
admin.site.register(CuentaCorriente)
admin.site.register(FacturaComision)
admin.site.register(Nota)