"""hms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from patient.views import index, home, patient_list, add_patient, edit_patient, discharge_patient, hms_logout, hms_login


urlpatterns = [
	path('', index),
    path(r'login', hms_login),
    path(r'logout', hms_logout),
    path(r'home', home),
    path(r'patient_list', patient_list),
    path(r'add_patient', add_patient),
    path(r'edit_patient/<int:id>', edit_patient),
    path(r'discharge_patient/<int:id>', discharge_patient),
    path('admin/', admin.site.urls),
]
