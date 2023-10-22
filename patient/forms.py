from django import forms
from django.forms import ModelForm
from patient.models import Patient


class PatientForm(ModelForm):

	def clean_contact_number(self):
		clean_data = self.clean()
		contact_number = clean_data.get('contact_number')
		if not contact_number.isdigit() or len(contact_number) > 10:
			self.add_error('contact_number', 'Invalid contact number')
		if Patient.objects.filter(contact_number=contact_number).exists():
			self.add_error('contact_number', 'contact_number already exist')
	class Meta:
		model = Patient
		fields = ['first_name', 'last_name', 'dob', 'contact_number', 'admission_date', 'ward_number']
		widgets = {
            'dob': forms.widgets.DateInput(attrs={'type': 'date'}),
            'admission_date': forms.widgets.DateInput(attrs={'type': 'date'}),
        }