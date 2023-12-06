from django.contrib import admin
from .models import TodoItem, Location, Item

# Register your models here.
admin.site.register(TodoItem)
admin.site.register(Location)
admin.site.register(Item)
