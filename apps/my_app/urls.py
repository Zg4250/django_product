from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('login', views.login),
    path('displaywishlist', views.displaywishlist),
    path('additem', views.additem),
    path('createitem', views.createitem),
    path('showitem/<id>', views.showitem),
    path('wishlist/<id>', views.wishlist),
    path('nonwishlist/<id>', views.nonwishlist),
    path('delete/<id>', views.delete),
    path('logout', views.logout)
]