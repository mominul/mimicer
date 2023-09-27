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
        
        return redirect(f'/patient/{subject_id}')
    return render(request, 'patient.html')

def admission_view(request, id):
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
        
        return redirect(f'/admission/{id}')
    data = {
        'subject_id': id,
    }
    return render(request, 'admission.html', data)

def modify_admission_view(request, id):
    if request.method == "POST":
        admission = Admission.objects.get(hadm_id=id)

        admission.admittime = request.POST.get('admittime')
        admission.dischtime = request.POST.get('dischtime')
        admission.deathtime = request.POST.get('deathtime')
        admission.admission_type = request.POST.get('admission_type')
        admission.admit_provider_id = request.POST.get('admit_provider_id')
        admission.admission_location = request.POST.get('admission_location')
        admission.discharge_location = request.POST.get('discharge_location')
        admission.insurance = request.POST.get('insurance')
        admission.language = request.POST.get('language')
        admission.marital_status = request.POST.get('marital_status')
        admission.race = request.POST.get('ethnicity')
        admission.edregtime = request.POST.get('edregtime')
        admission.edouttime = request.POST.get('edouttime')
        admission.hospital_expire_flag = request.POST.get('hospital_expire_flag')

        admission.save()

        return redirect(f'/admission/{admission.subject_id.subject_id}')

    admission = Admission.objects.get(hadm_id=id)
    data = admission.__dict__
    data['admittime'] = data['admittime'].strftime("%Y-%m-%dT%H:%M")
    data['dischtime'] = data['dischtime'].strftime("%Y-%m-%dT%H:%M")
    data['deathtime'] = data['deathtime'].strftime("%Y-%m-%dT%H:%M")
    data['edregtime'] = data['edregtime'].strftime("%Y-%m-%dT%H:%M")
    data['edouttime'] = data['edouttime'].strftime("%Y-%m-%dT%H:%M")
    return render(request, 'modify-admission.html', data)

def diagnosis_view(request, id):
    if request.method == 'POST':
        # subject_id = request.POST.get('subject_id')
        subject_id = Patient.objects.get(subject_id=id)
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
        
        return redirect(f'/diagnosis/{id}')
    return render(request, 'diagnosis.html')

def modify_diagnosis_view(request, id):
    if request.method == "POST":
        diagnosis = Diagnosis.objects.get(id=id)

        diagnosis.seq_num = request.POST.get('seq_num')
        diagnosis.icd_code = request.POST.get('icd_code')
        diagnosis.icd_version = request.POST.get('icd_version')
        diagnosis.icd_title = request.POST.get('icd_title')

        diagnosis.save()
        return redirect(f'/diagnosis/{diagnosis.subject_id.subject_id}')

    diagnosis = Diagnosis.objects.get(id=id)
    data = diagnosis.__dict__
    return render(request, 'modify-diagnosis.html', data)

def edstays_view(request, id):
    if request.method == 'POST':
        # subject_id = request.POST.get('subject_id')
        subject_id = Patient.objects.get(subject_id=id)
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
        
        return redirect(f'/edstays/{id}')
    return render(request, 'edstays.html')

def modify_edstays_view(request, id):
    if request.method == "POST":
        edstay = Edstay.objects.get(stay_id=id)

        edstay.intime = request.POST.get('intime')
        edstay.outtime = request.POST.get('outtime')
        edstay.gender = request.POST.get('gender')
        edstay.race = request.POST.get('race')
        edstay.arrival_transport = request.POST.get('arrival_transport')
        edstay.disposition = request.POST.get('disposition')

        edstay.save()
        return redirect(f'/edstays/{edstay.subject_id.subject_id}')

    edstay = Edstay.objects.get(stay_id=id)
    data = edstay.__dict__
    data['intime'] = data['intime'].strftime("%Y-%m-%dT%H:%M")
    data['outtime'] = data['outtime'].strftime("%Y-%m-%dT%H:%M")
    return render(request, 'modify-edstays.html', data)

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

def search_view(request):
    if request.method == "POST":
        search = request.POST["search"]
        try:
            patient = Patient.objects.get(subject_id=search)
            data = patient.__dict__
            return render(request, 'view-patient.html', data)
        except:
            messages.error(request, "Patient not found! Please create a new patient through this form!")
            return render(request, 'patient.html')
    
    return render(request, 'view-patient.html')

def view_patient_view(request, id):
    patient = Patient.objects.get(subject_id=id)
    data = patient.__dict__
    return render(request, 'view-patient.html', data)

def view_admission_view(request, id):
    admissions = Admission.objects.filter(subject_id=id)
    items = []
    for item in admissions:
        print(item.__dict__)
        items.append(item.__dict__)
    
    data = {
        'subject_id': id,
        'data': items
    }
    
    return render(request, 'view-admission.html', data)

def view_edstays_view(request, id):
    edstays = Edstay.objects.filter(subject_id=id)
    items = []
    for item in edstays:
        items.append(item.__dict__)
    
    data = {
        'subject_id': id,
        'data': items
    }
    
    return render(request, 'view-edstay.html', data)

def view_diagnosis_view(request, id):
    diagnosis = Diagnosis.objects.filter(subject_id=id)
    items = []
    for item in diagnosis:
        items.append(item.__dict__)
    
    data = {
        'subject_id': id,
        'data': items
    }
    
    return render(request, 'view-diagnosis.html', data)

def view_pyxis_view(request, id):
    pyxis = Pyxis.objects.filter(subject_id=id)
    items = []
    for item in pyxis:
        items.append(item.__dict__)
    
    data = {
        'subject_id': id,
        'data': items
    }
    
    return render(request, 'view-pyxis.html', data)

def view_triage_view(request, id):
    triage = Triage.objects.filter(subject_id=id)
    items = []
    for item in triage:
        print(item.__dict__)
        items.append(item.__dict__)
    
    data = {
        'subject_id': id,
        'data': items
    }
    
    return render(request, 'view-triage.html', data)
