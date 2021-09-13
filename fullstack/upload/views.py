from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage


@login_required  # decorator que exige login para acessar determinada url
def upload(request):
    context = {}
    if request.method == 'POST':  # upload sempre são feitos por POST
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        context['url'] = fs.url(name)
    return render(request, 'upload.html', context)

