from fullstack.core.forms import RoomForm
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View

from fullstack.core.forms import RoomForm
from fullstack.core.models import Room


class AddRoomView(View):
    room_form = RoomForm
    room_template = 'upload_room.html'

    @method_decorator(login_required)
    def get(self, request):
        form = self.room_form()
        return render(request, self.room_template, {'form': form})

    @method_decorator(login_required)
    def post(self, request):
        form = self.room_form(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('list')
        return render(request, self.room_template, {'form': form})


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
