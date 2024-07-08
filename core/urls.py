from core import views
from django.urls import path

app_name="core"

urlpatterns=[
    path("",views.index,name="index"),
    path('set_language/', views.set_language, name='set_language'),
]
