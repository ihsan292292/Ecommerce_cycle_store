from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name='index'),
    path('seller_login/',seller_log,name='seller_login'),
    path('seller_reg/',seller_reg,name='seller_reg'),
    path('product-add/',prod_add,name='product-add'),
    path('profile_page/',seller_profile,name='profile_page'),
    path('edit-profile/',edit_seller_profile,name='edit-profile'),
    path('view-product/',view_cycle_seller,name='seller-view-product'),
    path('edit-cycle/<int:id>',edit_cycle,name='edit-cycle'),
    path('delete-cycle/<int:id>',delete_cycle, name='delete-cycle'),
    path('logout-seller',seller_logout, name='seller-logout'),
    path('buyer-registration/',buy_reg,name='buyer-reg'),
    path('buyer-login/',buyer_log, name='buyer-log'),
    path('buyer-index-all/',buyer_index_all, name='buyer_index_all'),
    path('buyer-index-all/<url_variable>/',buyer_index_b_type,name='buyer-index'),
    # path('buyer-index-all/<agr>',buyer_index_age_range,name='buyer-index'),
    path('buyer-profile/',buyer_profile, name='buyer-profile'),
    path('buyer-logout',buyer_logout,name="buyer-logout"),
    path('add_wishList/<int:id>',add_wishlist, name="add_wishlist"),
    path('view_wishlist/',view_wishlist, name='view-wishlist'),
    path('delete_wishlist/<int:id>',delete_wishlist, name='delete-wishlist'),
    path("add_cart/<int:id>",add_cart,name="add-cart"),
    path('view_cart/',view_cart,name='view-cart'),
    path("delete_cart/<int:id>",delete_cart, name="delete_cart"),
    path('increment_cart_pro/<int:id>',increment_cart_pro, name="increment-pro"),
    path('decrement_cart_pro/<int:id>',decrement_cart_pro, name='decrement-pro'),
    path('delivery_details_add/',delivery_details_add, name='delivery_details_add'),
    path('order_success/',order_success, name="order_success"),
    path('view_total_orders/',view_orderd, name='view_total_order')
]