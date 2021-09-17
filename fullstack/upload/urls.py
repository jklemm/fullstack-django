from django.urls import path

from fullstack.upload import views

urlpatterns = [
    path('add', views.add_contract, name='add_contract'),
    path('list', views.list_contracts, name='contract'),
    path('delete/<int:pk>', views.delete_contract, name='delete_contract'),
]
