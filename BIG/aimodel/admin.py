from django.contrib import admin
from .models import *

# Register your models here.
class AimodelAdmin(admin.ModelAdmin):
    list_display = ('version', 'select', 'item', 'region','pub_date')    
admin.site.register(Aimodel , AimodelAdmin)