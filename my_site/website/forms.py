from django.forms import ModelForm, TextInput
from .models import Room, Meeting
from django.core.exceptions import ValidationError
from re import match


class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__'
        widgets = {
            'name': TextInput(attrs={'type': 'text'}),
            'floor': TextInput(attrs={'type': 'text'}),
            'room_number': TextInput(attrs={
                'type': 'number',
                'min': '101',
                'max': '501'
            })
        }

    def clean_name(self):
        name = self.cleaned_data.get('name')

        if not match(r'^[a-zA-Z0-9\s\-]*$', name):
            raise ValidationError('Room name has only digit, letters and "-" sembol.')
        return name

    def clean_floor(self):
        floor = self.cleaned_data.get('floor')

        for i in floor:
            if not i.isdigit():
                raise ValidationError('Floor cannot contains any character.')
        return floor








