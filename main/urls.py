from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.blogs, name='index'),
    path('blog-detail/<int:id>/', views.blog_detail, name='blog_detail'),
    path('comment/create/', views.comment_create, name='comment_create'),
    path('authenticate/', include('main.authentication.urls')),
    path('dashboard/', include('main.dashboard.urls'))
]