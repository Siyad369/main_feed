from django.urls import path
from . import views

urlpatterns = [
    path('feedback', views.submit_feedback, name='feedback'),
    path('show', views.show_feedback, name='show'),
    path('edit/<pk>', views.edit_feedback, name='edit'),
    path('delete/<pk>', views.delete_feedback, name='delete')

]
