from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View

from fullstack.core.forms import ContractForm
from fullstack.core.models import Contract


class AddContractView(View):
    contract_form = ContractForm
    contract_template = 'upload_contract.html'

    @method_decorator(login_required)
    def get(self, request):
        form = self.contract_form()
        return render(request, self.contract_template, {'form': form})

    @method_decorator(login_required)
    def post(self, request):
        form = self.contract_form(request.POST, request.FILES)
        if form.is_valid():
            Contract.objects.create(
                user_id=form.cleaned_data['Inquilino'],
                room_id=form.cleaned_data['Moradia'],
                residence_value=form.cleaned_data['Valor_aluguel'],
                rented_at=form.cleaned_data['Alugado_em'],
                contract=form.cleaned_data['Contrato_PDF']
            )
            return HttpResponseRedirect('list')
        return render(request, self.contract_template, {'form': form})


class ListContractView(View):
    contract_list = Contract
    contract_template = 'contracts.html'

    @method_decorator(login_required)
    def get(self, request):
        list_all_contracts = self.contract_list.objects.select_related('user', 'room').all()
        return render(request, self.contract_template, {'contracts': list_all_contracts})


class DeleteContractView(View):
    contract_list = Contract

    @method_decorator(login_required)
    def post(self, request, pk):
        contract = self.contract_list.objects.get(pk=pk)
        contract.delete()
        return redirect('contract')
