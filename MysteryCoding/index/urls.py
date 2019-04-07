from django.conf.urls import url
from django.urls import path
from index import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.log, name='login'),
    path('instruction/', views.instruction, name='instruction'),

]