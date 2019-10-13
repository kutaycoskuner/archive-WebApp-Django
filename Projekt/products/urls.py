from django.urls import path
from . import views # there is py library called views to prevent ambiguity


urlpatterns = [
    path('', views.index)
]