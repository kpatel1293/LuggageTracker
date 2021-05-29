from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Luggage) #this allows admin to add luggage object data on admin webpage
admin.site.register(Blocks)
admin.site.register(Airport) #this allows admin to add airport object data on admin webpage
