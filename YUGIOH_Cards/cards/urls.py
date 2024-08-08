from django.urls import path
from . import views


urlpatterns =[
    path('',views.exibir_card,name = "homepage"),
    path('info_card/<int:id>/',views.info_card,name = "info_Cards"),
]