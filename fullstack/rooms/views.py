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
        return render(request, self.room_template, {'form': form, 'image_form': self.image_form})

    @method_decorator(login_required)
    def post(self, request):
        form = self.room_form(request.POST, request.FILES)
        image_form = self.image_form(request.POST, request.FILES)
        if form.is_valid():
            room_form = form.save()
            image_form.save()
            image = RoomImage.objects.get(id=id)
            room_form.image.add(image)
            return HttpResponseRedirect('list')
        return render(request, self.room_template, {'form': {form}, 'image_form': {image_form}})


class ListRoomsView(View):
    rooms_list = Room
    rooms_template = 'rooms.html'

    @method_decorator(login_required)
    def get(self, request):
        list_all_rooms = self.rooms_list.objects.all()
        return render(request, self.rooms_template, {'rooms': list_all_rooms})


class DeleteRoomView(View):
    rooms_list = Room

    @method_decorator(login_required)
    def post(self, request, pk):
        room = self.rooms_list.objects.get(pk=pk)
        room.delete()
        return redirect('room')
