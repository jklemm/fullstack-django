from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from fullstack.core.models import Contract

# def create_residence:
# def residence_list:


@login_required
def contract_list(request):
    contracts = Contract.objects.all()
    return render(request, 'contracts.html', {
        'contracts': contracts
    })
