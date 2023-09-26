from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from django.contrib import messages
from .models import Patient, Admission, Diagnosis, Edstay, Pyxis, Triage

def login_view(request):
    if not request.user.is_authenticated:  
        if request.method == 'POST':
            email = request.POST['email']
            password = request.POST['password']

            if User.objects.filter(email=email).exists():
                user = User.objects.get(email=email)
                if user.check_password(password):
                    login(request, user)
                    return render(request, 'home.html')
                else:
                    messages.error(request, "Incorrect password!")
                    return redirect('/')
            else:
                messages.error(request, "Unknown email, please request an signup first!")
                return redirect('/')
        
        return render(request, 'login.html')
    else:
        return render(request, 'home.html')

def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('/')

def patient_view(request):
    if request.method == 'POST':
        subject_id = request.POST.get('subject_id')
        gender = request.POST.get('gender')
        anchor_age = request.POST.get('anchor_age')
        anchor_year = request.POST.get('anchor_year')
        anchor_year_group = request.POST.get('anchor_year_group')
        dod = request.POST.get('dod')
        
        # Create and save a new Patient object
        patient = Patient(subject_id=subject_id, gender=gender, anchor_age=anchor_age,
                          anchor_year=anchor_year, anchor_year_group=anchor_year_group, dod=dod)
        patient.save()
        
        return redirect('/')
    return render(request, 'patient.html')

def admission_view(request):
    if request.method == 'POST':
        subject_id = request.POST.get('subject_id')
        subject_id = Patient.objects.get(subject_id=subject_id)
        hadm_id = request.POST.get('hadm_id')
        admittime = request.POST.get('admittime')
        dischtime = request.POST.get('dischtime')
        deathtime = request.POST.get('deathtime')
        admission_type = request.POST.get('admission_type')
        admit_provider_id = request.POST.get('admit_provider_id')
        admission_location = request.POST.get('admission_location')
        discharge_location = request.POST.get('discharge_location')
        insurance = request.POST.get('insurance')
        language = request.POST.get('language')
        marital_status = request.POST.get('marital_status')
        race = request.POST.get('ethnicity')
        edregtime = request.POST.get('edregtime')
        edouttime = request.POST.get('edouttime')
        hospital_expire_flag = request.POST.get('hospital_expire_flag')
        
        # Create and save a new Admission object
        admission = Admission(subject_id=subject_id, hadm_id=hadm_id, admittime=admittime,
                              dischtime=dischtime, deathtime=deathtime, admission_type=admission_type,
                              admit_provider_id=admit_provider_id, admission_location=admission_location,
                              discharge_location=discharge_location, insurance=insurance, language=language,
                              marital_status=marital_status, race=race, edregtime=edregtime,
                              edouttime=edouttime, hospital_expire_flag=hospital_expire_flag)
        admission.save()
        
        return redirect('/')
    return render(request, 'admission.html')

def diagnosis_view(request):
    if request.method == 'POST':
        subject_id = request.POST.get('subject_id')
        subject_id = Patient.objects.get(subject_id=subject_id)
        stay_id = request.POST.get('stay_id')
        stay_id = Edstay.objects.get(stay_id=stay_id)
        seq_num = request.POST.get('seq_num')
        icd_code = request.POST.get('icd_code')
        icd_version = request.POST.get('icd_version')
        icd_title = request.POST.get('icd_title')
        
        # Create and save a new Diagnosis object
        diagnosis = Diagnosis(subject_id=subject_id, stay_id=stay_id, seq_num=seq_num,
                              icd_code=icd_code, icd_version=icd_version, icd_title=icd_title)
        diagnosis.save()
        
        return redirect('/')
    return render(request, 'diagnosis.html')

def edstays_view(request):
    if request.method == 'POST':
        subject_id = request.POST.get('subject_id')
        subject_id = Patient.objects.get(subject_id=subject_id)
        hadm_id = request.POST.get('hadm_id')
        hadm_id = Admission.objects.get(hadm_id=hadm_id)
        stay_id = request.POST.get('stay_id')
        intime = request.POST.get('intime')
        outtime = request.POST.get('outtime')
        gender = request.POST.get('gender')
        race = request.POST.get('race')
        arrival_transport = request.POST.get('arrival_transport')
        disposition = request.POST.get('disposition')
        
        # Create and save a new Edstay object
        edstay = Edstay(subject_id=subject_id, hadm_id=hadm_id, stay_id=stay_id,
                        intime=intime, outtime=outtime, gender=gender, race=race,
                        arrival_transport=arrival_transport, disposition=disposition)
        edstay.save()
        
        return redirect('/')
    return render(request, 'edstays.html')

def pyxis_view(request):
    if request.method == 'POST':
        subject_id = request.POST.get('subject_id')
        subject_id = Patient.objects.get(subject_id=subject_id)
        stay_id = request.POST.get('stay_id')
        stay_id = Edstay.objects.get(stay_id=stay_id)
        charttime = request.POST.get('charttime')
        med_rn = request.POST.get('med_rn')
        name = request.POST.get('name')
        gsn_rn = request.POST.get('gsn_rn')
        gsn = request.POST.get('gsn')
        
        # Create and save a new Pyxis object
        pyxis = Pyxis(subject_id=subject_id, stay_id=stay_id, charttime=charttime,
                      med_rn=med_rn, name=name, gsn_rn=gsn_rn, gsn=gsn)
        pyxis.save()
        
        return redirect('/')
    return render(request, 'pyxis.html')

def triage_view(request):
    if request.method == 'POST':
        subject_id = request.POST.get('subject_id')
        subject_id = Patient.objects.get(subject_id=subject_id)
        stay_id = request.POST.get('stay_id')
        stay_id = Edstay.objects.get(stay_id=stay_id)
        temperature = request.POST.get('temperature')
        heartrate = request.POST.get('heartrate')
        resprate = request.POST.get('resprate')
        o2sat = request.POST.get('o2sat')
        sbp = request.POST.get('sbp')
        dbp = request.POST.get('dbp')
        pain = request.POST.get('pain')
        acuity = request.POST.get('acuity')
        chiefcomplaint = request.POST.get('chiefcomplaint')
        
        # Create and save a new Triage object
        triage = Triage(subject_id=subject_id, stay_id=stay_id, temperature=temperature,
                        heartrate=heartrate, resprate=resprate, o2sat=o2sat, sbp=sbp,
                        dbp=dbp, pain=pain, acuity=acuity, chiefcomplaint=chiefcomplaint)
        triage.save()
        
        return redirect('/')
    return render(request, 'triage.html')
