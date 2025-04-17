from django.urls import path
from hospital.views import oftalmologia, pediatria, cirujia, psiquiatria

app_name = "hospital"


urlpatterns = [
    path("oftalmologia", oftalmologia, name="oftalmologia"),
    path("pediatria", pediatria, name="pediatria" ),
    path("cirujia", cirujia, name="cirujia"),
    path("psiquiatria", psiquiatria, name="psiquiatria" ),
]