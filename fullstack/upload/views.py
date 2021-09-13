from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from fullstack.core.forms import ContractForm


@login_required  # decorator que exige login para acessar determinada url
def upload(request):
    if request.method == 'POST':
        form = ContractForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('contract')
    else:
        form = ContractForm()
    return render(request, 'upload.html', {
        'form': form
    })
