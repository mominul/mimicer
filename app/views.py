from django.shortcuts import render

def patient_view(request):
    return render(request, 'patient.html')

def admission_view(request):
    return render(request, 'admission.html')

def diagnosis_view(request):
    return render(request, 'diagnosis.html')

def edstays_view(request):
    return render(request, 'edstays.html')

def pyxis_view(request):
    return render(request, 'pyxis.html')

def triage_view(request):
    return render(request, 'triage.html')
