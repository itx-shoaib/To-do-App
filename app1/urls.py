# We have created this file by our own to make path for app1.urls
from django.urls import path
from . import views

urlpatterns = [

    path('save/', views.save, name='save'),
    path('delete/<int:id>', views.delete),
    path('finish/', views.finish),

    path('', views.home, name='home'),
]
