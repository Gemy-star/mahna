from django import forms
from . import models


class ProofForm(forms.ModelForm):
    class Meta:
        model = models.ProfessionProof
        fields = ['professionNumber', 'date']
        widgets = {
            'professionNumber': forms.TextInput(
                attrs={'id': 'professionfield', 'class': 'form-control', 'placeholder': 'رقم صك الملكية '}),
            'date': forms.SelectDateWidget(
                attrs={'id': 'datefield', 'class': 'form-control', 'placeholder': 'التاريخ '}),
        }


class FloorForm(forms.ModelForm):
    class Meta:
        model = models.ConstructionFloor
        fields = ['floorNumber', 'area']
        widgets = {
            'floorNumber': forms.TextInput(
                attrs={'id': 'floorfield', 'class': 'form-control', 'placeholder': 'رقم الدور '}),
            'area': forms.NumberInput(
                attrs={'id': 'areafield', 'class': 'form-control', 'placeholder': 'المساحة '}),
        }


class ConstructionForm(forms.ModelForm):
    class Meta:
        model = models.ConstructionLicense
        fields = ['buildingSurfaces', 'licenseNumber', 'usage', 'floors', 'date']
        widgets = {
            'buildingSurfaces': forms.TextInput(
                attrs={'id': 'buildingSurfacesfield', 'class': 'form-control', 'placeholder': 'مسطحات البناء'}),
            'licenseNumber': forms.NumberInput(
                attrs={'id': 'licenseNumberfield', 'class': 'form-control', 'placeholder': 'رقم الرخصة  '}),
            'usage': forms.TextInput(attrs={'id': 'usagefield', 'class': 'form-control', 'placeholder': 'الأستخدام'}),
            'date': forms.DateInput(attrs={'id': 'datefield', 'class': 'form-control', 'placeholder': 'تاريخ الرخصة '}),
            'floors': forms.CheckboxSelectMultiple(choices=models.ConstructionFloor.objects.all())
        }



class PrfoesssionForm(forms.ModelForm):
    class Meta:
        model = models.ProfessionDocument
        fields = ['city', 'district', 'apartmentArea', 'apartmentNumber', 'areaNumber', 'plannedNumber', 'proof']
        widgets = {
            'apartmentNumber': forms.NumberInput(
                attrs={'id': 'apartmentfield', 'class': 'form-control', 'placeholder': 'رقم الشقة '}),
            'apartmentArea': forms.NumberInput(
                attrs={'id': 'areafield', 'class': 'form-control', 'placeholder': 'مساحة الشقة  '}),
            'district': forms.TextInput(attrs={'id': 'districtfield', 'class': 'form-control', 'placeholder': 'الحي'}),
            'areaNumber': forms.TextInput(
                attrs={'id': 'areaNumberfield', 'class': 'form-control', 'placeholder': 'رقم القطعة'}),
            'plannedNumber': forms.TextInput(
                attrs={'id': 'palnfield', 'class': 'form-control', 'placeholder': 'رقم المخطط'}),
            'city': forms.TextInput(attrs={'id': 'cityfield', 'class': 'form-control', 'placeholder': 'المدينة'}),
            'proof': forms.CheckboxSelectMultiple(choices=models.ProfessionProof.objects.all())
        }


class ApplicantForm(forms.ModelForm):
    class Meta:
        model = models.Applicant
        fields = ['name', 'manager', 'phone', 'fax', 'address', 'recordCivilian']
        widgets = {
            'name': forms.TextInput(
                attrs={'id': 'namefield', 'class': 'form-control', 'placeholder': 'الأسم'}),
            'manager': forms.TextInput(
                attrs={'id': 'managerfield', 'class': 'form-control', 'placeholder': 'المسئول'}),
            'phone': forms.NumberInput(attrs={'id': 'phonefield', 'class': 'form-control', 'placeholder': 'الجوال'}),
            'fax': forms.TextInput(
                attrs={'id': 'faxfield', 'class': 'form-control', 'placeholder': 'الفاكس'}),
            'address': forms.TextInput(
                attrs={'id': 'addressfield', 'class': 'form-control', 'placeholder': 'العنوان'}),
            'city': forms.TextInput(attrs={'id': 'cityfield', 'class': 'form-control', 'placeholder': 'المدينة'}),
            'recordCivilian': forms.TextInput(
                attrs={'id': 'recordCivilianfield', 'class': 'form-control', 'placeholder': 'سجل مدنى'}),
        }
