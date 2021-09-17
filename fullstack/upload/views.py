from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from fullstack.core.forms import ContractForm
from fullstack.core.models import Contract


@login_required  # decorator que exige login para acessar determinada url
def add_contract(request):
    if request.method == 'POST':
        form = ContractForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('contract')
    else:
        form = ContractForm()
    return render(request, 'upload_form.html', {
        'form': form
    })


@login_required
def list_contracts(request):
    contracts = Contract.objects.all()
    return render(request, 'contracts.html', {
        'contracts': contracts
    })


@login_required()
def delete_contract(request, pk):
    if request.method == 'POST':
        contract = Contract.objects.get(pk=pk)
        contract.delete()
    return redirect('contract')
