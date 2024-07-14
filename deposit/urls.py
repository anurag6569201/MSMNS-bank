from django.urls import path
from deposit import views
app_name="deposit"

urlpatterns=[
    path("",views.saving,name="saving"),
    path("rates/",views.int_rate,name="int_rate"),
]
