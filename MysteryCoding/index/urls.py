from django.conf.urls import url
from django.urls import path
from index import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='index/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='index/logout.html'), name='logout'),
    path('instruction/', views.instruction, name='instruction'),

]