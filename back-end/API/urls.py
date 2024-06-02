from django.urls import path
from . import views
urlpatterns = [
    path('USER/', views.user_manager),
]