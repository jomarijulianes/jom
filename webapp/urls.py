from django.urls import path
from . import views


urlpatterns = [
    path('',views.index, name="index"),
    path('about/',views.aboutpage, name="about"),
    path('services/',views.servicespage, name="services"),
    path('contact/', views.contactpage, name="contact"),

]