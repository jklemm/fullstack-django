from django.urls import path

from fullstack.payments import views

urlpatterns = [
    path('', views.payments, name='payment'),

]
