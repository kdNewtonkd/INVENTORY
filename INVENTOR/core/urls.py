from django.urls import path
from .import views

urlpatterns=[
    path("index/",views.index,name='index'),
    path("staff/",views.staff,name='staff'),
    path("product/",views.product,name='product'),
    path("delete/<int:pk>",views.delete_product,name='delete_product'),
    #path('delete/<int:pk>/', views.delete_product, name='delete_product'),
    path("update/<int:pk>",views.update_product,name='update_product'),
     path("detail/<int:pk>",views.staff_detail,name='staff_detail'),

    path("order/",views.order,name='order')
]