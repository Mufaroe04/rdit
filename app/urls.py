from django.urls import path, include
from . import views
urlpatterns =[
        path('login/',views.login,name='login'),
        path('logout/',views.logout,name='logout'),
        path('register/',views.register,name='register'),
        path('blog/',views.blog,name='blog'),
        path('admin/',views.Admin,name='admin'),
        path('admin/',views.Admin,name='admin'),
        path('delete/<str:pk>/',views.delete,name='delete'),
        path('update-blog/<str:pk>/',views.update_blog,name='update-blog'),
        path('profile/',views.profile,name='profile'),
        path('read/<str:pk>/',views.read,name='read'),
        



]