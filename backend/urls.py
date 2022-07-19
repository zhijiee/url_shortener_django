from django.urls import path 

from . import views

urlpatterns = [
    path('testview', views.UrlListCreate.as_view()),
]
