from django.contrib import admin
from .models import Vegetable
 
@admin.register(Vegetable)
class VegetableAdmin(admin.ModelAdmin):
    # Define the fields to be displayed in the list view
    list_display = ('name', 'category', 'rate', 'weight')