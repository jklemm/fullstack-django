from django.urls import path

from fullstack.core import views

urlpatterns = [
    path('', views.contract_list, name='contract'),
]
