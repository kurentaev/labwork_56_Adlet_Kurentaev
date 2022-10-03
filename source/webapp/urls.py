from django.urls import path

from webapp.views.base import index_view
from webapp.views.products import product_view
from webapp.views.products import add_view
from webapp.views.products import update_view
# from webapp.views.guests import delete_view
# from webapp.views.guests import confirm_delete


urlpatterns = [
    path('', index_view, name='index'),
    path('products/', index_view, name='index_view'),
    path('products/<int:pk>', product_view, name='product_detail'),
    path('products/add/', add_view, name='product_add'),
    path('products/update/<int:pk>', update_view, name='product_update'),
    # path('guest_book/delete/<int:pk>', delete_view, name='guest_delete'),
    # path('guest_book/confirm_delete/<int:pk>', confirm_delete, name='confirm_delete')
]
