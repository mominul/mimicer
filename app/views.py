from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout

def login_view(request):
    if not request.user.is_authenticated:
        print("Not Authenticated!")    
        if request.method == 'POST':
            email = request.POST['email']
            password = request.POST['password']

            if User.objects.filter(email=email).exists():
                user = User.objects.get(email=email)
                if user.check_password(password):
                    login(request, user)
                    return render(request, 'home.html')
                else:
                    return render(request, 'login.html')
            else:
                return render(request, 'login.html')
        
        return render(request, 'login.html')
    else:
        return render(request, 'home.html')

def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('/')

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
