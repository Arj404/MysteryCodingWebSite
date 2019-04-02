from django.conf.urls import url
from index import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^$', views.log, name='login'),
    url(r'^$', views.instruction, name='instruction'),

]