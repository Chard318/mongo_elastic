from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('search', views.search, name='search'),
    path('profile/<title>', views.profile, name='profile'),
    path('item/<document>', views.item, name='item')
    #path('profile', views.profile, name='profile'),
]