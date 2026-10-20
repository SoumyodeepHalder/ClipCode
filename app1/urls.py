from django.urls import path
from app1 import views

app_name='app1'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:todo_id>/delete', views.delete, name='delete'),
    path('add', views.add, name='add'),
    path('addpage', views.addpage, name='addpage')
]