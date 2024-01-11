from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.todo,name="todo"),
    path('create/',views.form,name="form"),
    path('edit/<str:pk>/',views.edit,name='edit'),
    path('delete/<str:pk>/',views.delete,name='delete'),
]
