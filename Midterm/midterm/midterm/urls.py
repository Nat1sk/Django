from django.urls import path
from . import views

urlpatterns = [
    path('api/blogs', views.blogs, name='blogs'),
    path('api/blogs/:id/<int:pk>', views.blog, name='blog'),
    
]
