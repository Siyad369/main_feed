from django.urls import path
from . import views

urlpatterns = [
    path('feedback', views.submit_feedback, name='feedback'),
    path('show', views.show_feedback, name='show'),
    path('edit/<pk>', views.edit_feedback, name='edit'),
    path('delete/<pk>', views.delete_feedback, name='delete'),
    path('', views.sign_up, name='signup'),
    path('signin', views.sign_in, name='signin'),
    path('sign_out', views.sign_out, name='sign_out'),


]
