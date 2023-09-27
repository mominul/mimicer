"""
URL configuration for mimicer project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login_view, name="home"),
    path('search/', search_view),
    path('patient/<int:id>', view_patient_view, name='patient_view'),
    path('admission/<int:id>', view_admission_view, name='admission_view'),
    path('edstays/<int:id>', view_edstays_view, name='edstays_view'),
    path('diagnosis/<int:id>', view_diagnosis_view, name='diagnosis_view'),
    path('pyxis/<int:id>', view_pyxis_view, name='pyxis_view'),
    path('triage/<int:id>', view_triage_view, name='triage_view'),
    path('logout/', logout_view, name='logout'),
    path('entry/patient/', patient_view, name='patient_form'),
    path('entry/admission/<int:id>', admission_view, name='admission_form'),
    path('modify/admission/<int:id>', modify_admission_view, name='admission_modify'),
    path('diagnosis/', diagnosis_view, name='diagnosis_form'),
    path('edstays/', edstays_view, name='edstays_form'),
    path('pyxis/', pyxis_view, name='pyxis_form'),
    path('triage/', triage_view, name='triage_form'),
]
