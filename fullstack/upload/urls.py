from django.urls import path

from fullstack.upload import views

urlpatterns = [
    path('add', views.AddContractView.as_view(), name='add_contract'),
    path('list', views.ListContractView.as_view(), name='contract'),
    path('delete/<int:pk>', views.DeleteContractView.as_view(), name='delete_contract'),
]
