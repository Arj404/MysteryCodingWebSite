from django.urls import path
from index import views
from django.contrib.auth import views as auth_views
from django.conf.urls import include


urlpatterns = [
    path('', views.index, name='index'),
    path('', include('django.contrib.auth.urls')),
    path('register/', views.form, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('instruction/', views.instruction, name='instruction'),

]

