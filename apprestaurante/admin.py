from django.contrib import admin
from apprestaurante.models import Plato, PlatoAdmin, EmpleadoAdmin, Empleado, Cliente, ClienteAdmin, Menu, MenuAdmin

admin.site.register(Plato, PlatoAdmin)
admin.site.register(Empleado, EmpleadoAdmin)
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Menu, MenuAdmin)
