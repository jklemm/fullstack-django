from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views import View

from fullstack.contracts.gateway import create_contract, get_all_contracts, filter_contracts, delete_contract
from fullstack.core.forms import ContractForm


class AddContractView(View):
    @method_decorator(login_required)
    def get(self, request):
        form = ContractForm()
        return render(request, 'upload_contract.html', {'form': form})

    @method_decorator(login_required)
    def post(self, request):
        form = ContractForm(request.POST, request.FILES)
        if form.is_valid():
            inquilino = form.cleaned_data['Inquilino']
            moradia = form.cleaned_data['Moradia']
            valor_aluguel = form.cleaned_data['Valor_aluguel']
            alugado_em = form.cleaned_data['Alugado_em']
            contrato_pdf = form.cleaned_data['Contrato_PDF']
            create_contract(inquilino, moradia, valor_aluguel, alugado_em, contrato_pdf)
            return HttpResponseRedirect('list')
        return render(request, 'upload_contract.html', {'form': form})


class ListContractView(View):
    @method_decorator(login_required)
    def get(self, request):
        user = request.user
        if user.is_staff:
            contracts = get_all_contracts()
        else:
            contracts = filter_contracts(user.id)
        return render(request, 'contracts.html', {'contracts': contracts})


class DeleteContractView(View):
    @method_decorator(login_required)
    def post(self, request, pk):
        delete_contract(pk)
        return redirect('contract')
