from django.urls import path
from . import views

urlpatterns = [
    path('feedback', views.submit_feedback, name='feedback')

]
