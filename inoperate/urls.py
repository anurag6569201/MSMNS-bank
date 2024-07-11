from inoperate import views
from django.urls import path

app_name="inoperate"

urlpatterns=[
    path("",views.inoperate,name="inoperate"),
]
