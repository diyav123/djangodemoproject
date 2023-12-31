from app.models import Cinema
from django import forms


class cinemaform(forms.ModelForm):
    class Meta:
        model=Cinema
        fields='__all__'