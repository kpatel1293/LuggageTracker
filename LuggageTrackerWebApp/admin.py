from django.contrib import admin
from .models import LuggageBlockchain, luggage

# Register your models here.
admin.site.register(luggage) #this allows admin to add luggage object datas on admin webpage
admin.site.register(LuggageBlockchain)