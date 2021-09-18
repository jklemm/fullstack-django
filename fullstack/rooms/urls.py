from django.urls import path

from fullstack.rooms import views

urlpatterns = [
    path('add', views.AddRoomView.as_view(), name='add_room'),
    path('list', views.ListRoomsView.as_view(), name='room'),
    path('delete/<int:pk>', views.DeleteRoomView.as_view(), name='delete_room'),
]
