from django.contrib import admin
from .models import luggage
from .models import airport

# Register your models here.
admin.site.register(luggage) #this allows admin to add luggage object data on admin webpage
admin.site.register(airport) #this allows admin to add airport object data on admin webpage
