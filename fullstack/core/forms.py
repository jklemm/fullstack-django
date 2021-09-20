from django import forms

from .models import Contract, Room, RoomImage


class ContractForm(forms.ModelForm):
    class Meta:
        model = Contract
        fields = ('contract', 'residence_value', 'rented_at')

class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ('name', 'description', 'value','available')

class ImageForm(forms.ModelForm):
    class Meta:
        model = RoomImage
        fields = ('image',)