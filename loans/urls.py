from loans import views
from django.urls import path

app_name="loans"

urlpatterns=[
    path("property/",views.property,name="property"),
    path("home/",views.home,name="home"),
]
