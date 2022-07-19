from django.urls import path 

from . import views

urlpatterns = [
    path('testview', views.UrlListCreate.as_view()),
    path('api/shorten/', views.shorten_url),
    path('<str:hash>', views.redirect_hash, name='redirect')
]
