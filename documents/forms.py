from django import forms
from . import models


class PrfoesssionForm(forms.ModelForm):
    class Meta:
        model = models.ProfessionDocument
        fields = ['city', 'district', 'apartmentArea', 'apartmentNumber', 'areaNumber', 'plannedNumber','date' , 'professionNumber' ]
        widgets = {
            'apartmentNumber': forms.NumberInput(
                attrs={'id': 'apartmentfield', 'class': 'form-control', 'placeholder':  'رقم الشقة '}),
            'apartmentArea': forms.NumberInput(
                attrs={'id': 'areafield', 'class': 'form-control', 'placeholder': 'مساحة الشقة  '}),
            'district': forms.TextInput(attrs={'id': 'districtfield', 'class': 'form-control', 'placeholder': 'الحي'}),
            'areaNumber': forms.TextInput(
                attrs={'id': 'areaNumberfield', 'class': 'form-control', 'placeholder': 'رقم القطعة'}),
            'plannedNumber': forms.TextInput(
                attrs={'id': 'palnfield', 'class': 'form-control', 'placeholder': 'رقم المخطط'}),
            'city': forms.TextInput(attrs={'id': 'cityfield', 'class': 'form-control', 'placeholder': 'المدينة'}),
            'professionNumber': forms.NumberInput(
                attrs={'id': 'profNumfield', 'class': 'form-control', 'placeholder': 'رقم صك الملكية'}),
            'date': forms.SelectDateWidget(
                attrs={'id': 'date', 'class': 'form-control', 'placeholder': 'التاريخ'}),
        }
