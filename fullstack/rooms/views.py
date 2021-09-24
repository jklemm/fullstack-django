from fullstack.core.forms import RoomForm
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View

from fullstack.core.forms import RoomForm, ImageForm
from fullstack.core.models import Room, RoomImage


class AddRoomView(View):
    room_form = RoomForm
    image_form = ImageForm
    room_template = 'upload_room.html'

    @method_decorator(login_required)
    def get(self, request):
        form = self.room_form()
        return render(request, self.room_template, {'form': form, 'image': self.image_form})

    @method_decorator(login_required)
    def post(self, request):
        form = self.room_form(request.POST)
        image_form = self.image_form(request.POST, request.FILES)
        if form.is_valid() and image_form.is_valid():
            room = Room.objects.create(
                name=form.cleaned_data['Moradia'],
                description=form.cleaned_data['Descricao'],
                value=form.cleaned_data['Valor'],
                available=form.cleaned_data['Disponibilidade'],
            )
            RoomImage.objects.create(
                room=room,
                image=image_form.cleaned_data['image']
            )
            return HttpResponseRedirect('list')
        return render(request, self.room_template, {'form': form, 'image': image_form})


class ListRoomsView(View):
    rooms_list = Room
    images_list = RoomImage
    rooms_template = 'rooms.html'

    @method_decorator(login_required)
    def get(self, request):
        list_all_rooms = self.rooms_list.objects.all()
        list_all_images = self.images_list.objects.all()
        return render(request, self.rooms_template, {'rooms': list_all_rooms, 'images': list_all_images})


class DeleteRoomView(View):
    rooms_list = Room

    @method_decorator(login_required)
    def post(self, request, pk):
        room = self.rooms_list.objects.get(pk=pk)
        room.delete()
        return redirect('room')
