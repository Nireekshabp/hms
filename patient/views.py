from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from patient.models import Patient
from patient.forms import PatientForm


# Need to add logger

@login_required
def hms_logout(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return HttpResponseRedirect('/')



def hms_login(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/home')

    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                messages.success(request, f"Hello <b>{user.username}</b>! You have been logged in")
                return HttpResponseRedirect('/home')

        else:
            for error in list(form.errors.values()):
                messages.error(request, error) 

    form = AuthenticationForm() 
    
    return render(
        request=request,
        template_name="login.html", 
        context={'form': form}
        )



def index(request):
    return render(request,'index.html')



def home(request):
    return render(request,'home.html')



@login_required
def patient_list(request):
    patient_list = Patient.objects.filter(is_discharged=False)
    return render(request,'patient_list.html', {'patient_list': patient_list})


def get_incremented_patient_id(patient_id):
    suffix = int(patient_id[-4:])
    prefix = patient_id[0]
    suffix += 1
    incremented_patient_id = prefix + str(suffix).zfill(4)
    return incremented_patient_id



@login_required
def add_patient(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            if Patient.objects.count() == 0:
                f.patient_id = 'P0001'
            else:
                obj = Patient.objects.last()
                f.patient_id = get_incremented_patient_id(obj.patient_id)
            f.save()
            return HttpResponseRedirect('/patient_list')
    else:
        form = PatientForm()
        return render(request,'add_patient.html', {'form': form})


def edit_patient(request, id):
    patient = get_object_or_404(Patient, id=id)

    if request.method == 'GET':
        context = {'form': PatientForm(instance=patient), 'id': id}
        return render(request,'edit_patient.html',context)

    elif request.method == 'POST':
        form = PatientForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            messages.success(request, 'Patient details updated successfully.')
            return HttpResponseRedirect('/patient_list')
        else:
            messages.error(request, 'Please correct the following errors:')
            return render(request,'edit_patient.html',{'form':form})


def discharge_patient(request, id):
    patient = get_object_or_404(Patient, id=id)
    if request.method == 'GET':
        context = {'patient':patient ,'id': id}
        return render(request,'discharge_patient.html',context)

    elif request.method == 'POST':
        patient.is_discharged = True
        patient.save()
        messages.success(request, 'Patient discharged successfully.')
        return HttpResponseRedirect('/patient_list')