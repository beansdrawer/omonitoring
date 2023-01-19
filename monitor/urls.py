from django.urls import path

from . import views

urlpatterns = [
    path('maker/', views.maker, name='maker'),
    path('monitor/', views.monitor, name='monitor'),
    path('monitor/<int:pk>/', views.monitor_detail, name='monitor_detail'),
    path('spec/', views.spec, name='spec'),
    path('', views.index, name='index')
]