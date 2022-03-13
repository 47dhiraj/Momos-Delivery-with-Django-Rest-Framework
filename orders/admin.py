from django.contrib import admin

from .models import Order

# Register your models here.

@admin.register(Order)                                                          # registering the Order model in admin panel
class OrderAdmin(admin.ModelAdmin):                                             # customising admin panel for orders
    list_display = ['id', 'order_status', 'flavour', 'size', 'plate_quantity', 'customer', 'placed_at']  # yo list ma vako kura as a field chai admin panel ma display garni vaneko
    list_filter = ['placed_at','updated_at','order_status']                     # yaha mention gareko attribute or field ko basis ma orders record lai filter garna sakincha vaneko



 