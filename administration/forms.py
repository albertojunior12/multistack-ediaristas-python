from django import forms
from .models import Service
from decimal import Decimal


class ServiceForm(forms.ModelForm):
    min_value = forms.CharField(widget=forms.TextInput(attrs={"class": "money"}))
    commission_percentage = forms.CharField(widget=forms.TextInput(attrs={"class": "money"}))
    bedroom_value = forms.CharField(widget=forms.TextInput(attrs={"class": "money"}))
    living_room_value = forms.CharField(widget=forms.TextInput(attrs={"class": "money"}))
    bathroom_value = forms.CharField(widget=forms.TextInput(attrs={"class": "money"}))
    kitchen_value = forms.CharField(widget=forms.TextInput(attrs={"class": "money"}))
    backyard_value = forms.CharField(widget=forms.TextInput(attrs={"class": "money"}))
    other_value = forms.CharField(widget=forms.TextInput(attrs={"class": "money"}))

    class Meta:
        model = Service
        fields = '__all__'


    def clean_min_value(self):
        data = self.cleaned_data.get('min_value')
        return Decimal(data.replace(',', '.'))

    def clean_commission_percentage(self):
        data = self.cleaned_data.get('commission_percentage')
        return Decimal(data.replace(',', '.'))

    def clean_bedroom_value(self):
        data = self.cleaned_data.get('bedroom_value')
        return Decimal(data.replace(',', '.'))

    def clean_living_room_value(self):
        data = self.cleaned_data.get('living_room_value')
        return Decimal(data.replace(',', '.'))

    def clean_bathroom_value(self):
        data = self.cleaned_data.get('bathroom_value')
        return Decimal(data.replace(',', '.'))

    def clean_kitchen_value(self):
        data = self.cleaned_data.get('kitchen_value')
        return Decimal(data.replace(',', '.'))

    def clean_backyard_value(self):
        data = self.cleaned_data.get('backyard_value')
        return Decimal(data.replace(',', '.'))

    def clean_other_value(self):
        data = self.cleaned_data.get('other_value')
        return Decimal(data.replace(',', '.'))
