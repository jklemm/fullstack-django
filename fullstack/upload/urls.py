from django.urls import path

from fullstack.upload import views

urlpatterns = [
    path('', views.upload, name='upload'),
]
