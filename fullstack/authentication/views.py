from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


def home(request):
    count = User.objects.count()
    name = User.objects.first()
    return render(request, 'home.html', {
        'count': count,
        'name': name
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


@login_required  # decorator que exige login para acessar determinada url
def confidential_page(request):
    return render(request, 'confidential.html')
