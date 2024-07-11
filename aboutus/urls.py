from aboutus import views
from django.urls import path

app_name="aboutus"

urlpatterns=[
    path("profile",views.aboutmain,name="aboutmain"),
]
