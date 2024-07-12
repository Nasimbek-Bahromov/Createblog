from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.blog_create, name='blog_create'),
    path('update/<int:id>/', views.blog_update, name='blog_update'),
    path('delete/<int:id>/', views.blog_delete, name='blog_delete'),
    path('blogs/', views.my_blogs, name='my_blogs'),
]