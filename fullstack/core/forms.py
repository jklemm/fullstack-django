from django import forms
from django.contrib.auth.models import User

from fullstack.core.models import Room


class ContractForm(forms.Form):
    Inquilino = forms.ChoiceField(choices=[(u.id, u.username) for u in User.objects.all()])
    Moradia = forms.ChoiceField(choices=[(r.id, r.name) for r in Room.objects.all()])
    Valor_aluguel = forms.IntegerField()
    Alugado_em = forms.DateField()
    Contrato_PDF = forms.FileField()


class RoomForm(forms.Form):
    Moradia = forms.CharField()
    Descricao = forms.CharField(widget=forms.Textarea)
    Valor = forms.IntegerField()
    Disponibilidade = forms.BooleanField(initial=False, required=False)


class ImageForm(forms.Form):
    image = forms.ImageField()
