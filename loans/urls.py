from loans import views
from django.urls import path

app_name="loans"

urlpatterns=[
    path("property/",views.property,name="property"),
    path("home/",views.home,name="home"),
    path("emi/",views.emi_tool,name="emi_tool"),
    path("fdtool/",views.fd_tool,name="fd_tool"),
]
