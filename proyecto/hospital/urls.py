from django.urls import path
from hospital.views import oftalmologia


urlpatterns = [
    path("oftalmologia", oftalmologia )
]