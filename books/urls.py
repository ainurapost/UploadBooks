from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('detail/<int:book_id>', views.detail, name='detail'),
    path('new_list/>', views.new_list, name='new_list'),
    path('random_list/', views.random_list, name='random_list'),
    path('add/', views.add, name='add'),
]

