from django.contrib import admin
from inmuebleslist_app.models import Edificacion, Empresa, Comentario

# Register your models here.

admin.site.register(Edificacion)
admin.site.register(Comentario)
admin.site.register(Empresa)

