from django.contrib import admin
from django.urls import path
from . import views
import re

urlpatterns = [
    path('',views.index, name='index'),
    path('data/',views.add,name='add'),
    path('delete',views.delete,name='delete'),
    path('button',views.button,name='button'),
    # path('<book_id>/',views.detail, name='detail'),
]