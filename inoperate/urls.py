from inoperate import views
from django.urls import path

app_name="inoperate"

urlpatterns=[
    path("profile",views.inoperate,name="inoperate"),
]
