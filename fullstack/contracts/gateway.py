from datetime import date

from fullstack.core.models import Contract


def get_all_contracts():
    return Contract.objects.select_related('user', 'room').all()


def filter_contracts(user_id: int):
    return Contract.objects.select_related('user', 'room').filter(user_id=user_id)


def create_contract(user, room, residence_value, rented_at, contract):
    return Contract.objects.create(
        user=user,
        room=room,
        residence_value=residence_value,
        rented_at=rented_at,
        contract=contract
    )


def delete_contract(pk):
    contracts = Contract.objects.filter(pk=pk).update(
        closed_at=date.today(),
        active=False
    )
