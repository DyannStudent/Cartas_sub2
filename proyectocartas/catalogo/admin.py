from django.contrib import admin
from .models import cartas
from .models import Vendedor
from .models import Cliente

admin.site.register(cartas)

admin.site.register(Vendedor)

admin.site.register(Cliente)
