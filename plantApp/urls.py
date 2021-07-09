from django.urls import path
from . import views





app_name = 'plantApp'

urlpatterns = [
    path('', views.home, name = 'home'),
    path('upload/', views.upload, name = 'upload'),
    path('contact/', views.contact, name = 'contact'),
    path('result/', views.result, name = 'result'),

    path('test', views.Home.as_view(), name = 'home2'),
]
