from django.urls import path
from farmacia.views import recetas_magistrales


urlpatterns = [
    path("recetas_magistrales", recetas_magistrales )
]