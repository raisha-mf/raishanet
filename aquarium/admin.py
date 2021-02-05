from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Tank
from .models import TankDimensions
from .models import Fauna
from .models import Flora


admin.site.register(Tank)
admin.site.register(TankDimensions)
admin.site.register(Fauna)
admin.site.register(Flora)
