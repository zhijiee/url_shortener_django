from django.urls import path 

from . import views

urlpatterns = [
    path('shorten/<str:url>', views.shorten, name='shorten'),
    path('api/shorten/', views.UrlListCreate.as_view()),
]
