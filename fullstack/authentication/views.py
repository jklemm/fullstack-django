from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from fullstack.core.models import Room, RoomImage


def home(request):
    name = User.objects.first()
    list_all_rooms = Room.objects.all()
    list_all_images = RoomImage.objects.all()
    return render(request, 'home.html', {
        'name': name, 'rooms': list_all_rooms, 'images': list_all_images
    })


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {
        'form': form
    })
