from django.db import models

class Patient(models.Model):
    subject_id = models.IntegerField(primary_key=True)
    gender = models.CharField(max_length=1, null=False)
    anchor_age = models.IntegerField(null=False)
    anchor_year = models.IntegerField(null=False)
    anchor_year_group = models.CharField(max_length=255, null=False)
    dod = models.DateTimeField(null=True)

class Admission(models.Model):
    subject_id = models.ForeignKey(Patient, on_delete=models.CASCADE)
    hadm_id = models.IntegerField(primary_key=True)
    admittime = models.DateTimeField(null=False)
    dischtime = models.DateTimeField(null=True)
    deathtime = models.DateTimeField(null=True)
    admission_type = models.CharField(max_length=40, null=False)
    admit_provider_id = models.CharField(max_length=10, null=True)
    admission_location = models.CharField(max_length=60, null=True)
    discharge_location = models.CharField(max_length=60, null=True)
    insurance = models.CharField(max_length=255, null=True)
    language = models.CharField(max_length=10, null=True)
    marital_status = models.CharField(max_length=30, null=True)
    race = models.CharField(max_length=80, null=True)
    edregtime = models.DateTimeField(null=True)
    edouttime = models.DateTimeField(null=True)
    hospital_expire_flag = models.SmallIntegerField(null=True)

class Edstay(models.Model):
    subject_id = models.ForeignKey(Patient, on_delete=models.CASCADE)
    hadm_id = models.ForeignKey(Admission, on_delete=models.CASCADE, null=True)
    stay_id = models.IntegerField(primary_key=True)
    intime = models.DateTimeField(null=False)
    outtime = models.DateTimeField(null=False)
    gender = models.CharField(max_length=1, null=False)
    race = models.CharField(max_length=60, null=True)
    arrival_transport = models.CharField(max_length=50, null=False)
    disposition = models.CharField(max_length=255, null=True)

class Diagnosis(models.Model):
    subject_id = models.ForeignKey(Patient, on_delete=models.CASCADE)
    stay_id = models.ForeignKey(Edstay, on_delete=models.CASCADE)
    seq_num = models.IntegerField(null=False)
    icd_code = models.CharField(max_length=10, null=False)
    icd_version = models.IntegerField(null=False)
    icd_title = models.TextField(null=False)

class Pyxis(models.Model):
    subject_id = models.ForeignKey(Patient, on_delete=models.CASCADE)
    stay_id = models.ForeignKey(Edstay, on_delete=models.CASCADE)
    charttime = models.DateTimeField(null=True)
    med_rn = models.SmallIntegerField(null=False)
    name = models.CharField(max_length=255, null=True)
    gsn_rn = models.SmallIntegerField(null=False)
    gsn = models.CharField(max_length=10, null=True)

class Triage(models.Model):
    subject_id = models.ForeignKey(Patient, on_delete=models.CASCADE)
    stay_id = models.ForeignKey(Edstay, on_delete=models.CASCADE)
    temperature = models.DecimalField(max_digits=10, decimal_places=4, null=True)
    heartrate = models.DecimalField(max_digits=10, decimal_places=4, null=True)
    resprate = models.DecimalField(max_digits=10, decimal_places=4, null=True)
    o2sat = models.DecimalField(max_digits=10, decimal_places=4, null=True)
    sbp = models.DecimalField(max_digits=10, decimal_places=4, null=True)
    dbp = models.DecimalField(max_digits=10, decimal_places=4, null=True)
    pain = models.TextField(null=True)
    acuity = models.DecimalField(max_digits=10, decimal_places=4, null=True)
    chiefcomplaint = models.CharField(max_length=255, null=True)
