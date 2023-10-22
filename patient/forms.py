from django import forms
from django.forms import ModelForm
from patient.models import Patient


class PatientForm(ModelForm):
	class Meta:
		model = Patient
		fields = ['first_name', 'last_name', 'dob', 'contact_number', 'admission_date', 'ward_number']
		widgets = {
            'dob': forms.widgets.DateInput(attrs={'type': 'date'}),
            'admission_date': forms.widgets.DateInput(attrs={'type': 'date'}),
        }