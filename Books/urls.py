from django.contrib import admin
from django.urls import path
from Books import views

app_name = 'Books'

urlpatterns = [
    path('',views.index, name='index'),
    path('data/',views.add,name='add'),
    path('delete',views.delete,name='delete'),
    path('button1',views.button,name='button'),
    path('button',views.result,name='result'),
    # path('<book_id>/',views.detail, name='detail'),
]