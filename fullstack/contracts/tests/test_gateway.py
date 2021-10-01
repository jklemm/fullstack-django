from datetime import date

from django.core.files.uploadedfile import SimpleUploadedFile
from django.contrib.auth.models import User
from django.test import TestCase

from fullstack.contracts.gateway import get_all_contracts, filter_contracts, create_contract, delete_contract
from fullstack.core.models import Contract, Room


class GetAllContractsTest(TestCase):
    def test_should_return_all_contracts(self):
        Contract.objects.create(residence_value=1000, rented_at=date.today(), active=True)
        Contract.objects.create(residence_value=800, rented_at=date.today(), active=False)

        contracts = get_all_contracts()

        self.assertEqual(2, len(contracts))


class FilterContractsTest(TestCase):
    def test_should_filter_one_contract(self):
        user_1 = User.objects.create(username='user_1')
        user_2 = User.objects.create(username='user_2')
        Contract.objects.create(user_id=user_1.id, residence_value=1000, rented_at=date.today(), active=True)
        Contract.objects.create(user_id=user_2.id, residence_value=800, rented_at=date.today(), active=False)

        contracts = filter_contracts(user_1.id)

        self.assertEqual(1, len(contracts))
        self.assertEqual(user_1.id, contracts[0].user_id)


class CreateContractTest(TestCase):
    def test_should_create_one_contract(self):
        user = User.objects.create(username='user_1')
        room = Room.objects.create(value=1000)
        contract_pdf = SimpleUploadedFile("contract.pdf", b"huuurrrllll!", content_type='application/pdf')

        contract = create_contract(
            user=user, room=room, residence_value=1000, rented_at=date.today(), contract=contract_pdf
        )

        db_contract = Contract.objects.get(id=contract.id)
        self.assertEqual(contract.residence_value, db_contract.residence_value)
        self.assertEqual(contract.rented_at, db_contract.rented_at)


class DeleteContractTest(TestCase):
    def test_should_delete_contract(self):
        contract = Contract.objects.create(residence_value=800, rented_at=date.today(), active=True)

        delete_contract(contract.id)

        db_contract = Contract.objects.get(id=contract.id)
        self.assertIsNotNone(db_contract.closed_at)
        self.assertFalse(db_contract.active)
