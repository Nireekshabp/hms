from django.db import models

# Create your models here.


class Patient(models.Model):
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	patient_id = models.CharField(max_length=8, unique=True, blank=True, null=False)
	dob = models.DateField()
	contact_number = models.CharField(max_length=12)
	admission_date = models.DateField()
	ward_number = models.ForeignKey('ward.Ward', on_delete=models.SET_NULL,
                                    null=True, related_name='from_user')
	is_discharged = models.BooleanField(default=False)

	def __str__(self):
		return f"{self.first_name} {self.last_name}"
	
