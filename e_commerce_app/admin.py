from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(seller_register)
admin.site.register(add_product)
admin.site.register(buyer_register)
admin.site.register(wishlist)
admin.site.register(cart)
admin.site.register(delivary_details)


# django __str__()
# which is used to convert an object into string 