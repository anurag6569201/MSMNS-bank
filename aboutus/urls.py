from aboutus import views
from django.urls import path

app_name="aboutus"

urlpatterns=[
    path("profile",views.aboutmain,name="aboutmain"),
    path("health",views.financialhealth,name="financialhealth"),
    path("commitment",views.commitment,name="commitment"),
    path("chairman",views.chairman,name="chairman"),
    path("directors",views.directors,name="directors"),
]
