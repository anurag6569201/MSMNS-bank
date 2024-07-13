from inoperate import views
from django.urls import path

app_name="inoperate"

urlpatterns=[
    path("",views.inoperate,name="inoperate"),
    path("DEAF",views.view_full_deaf,name="view_full_deaf"),

    # authentication urls
    path('sign-in/',views.login_view,name='sign-in'),
    path('sign-out/',views.logout_view,name='sign-out'),

    # downloading full deaf in pdf
    path('generate-pdf/', views.generate_pdf, name='generate_pdf'),
]
