from core import views
from django.urls import path

app_name="core"

urlpatterns=[
    path("",views.index,name="index"),
    path("underwork/<str:data>", views.underwork, name="underwork"),
]
