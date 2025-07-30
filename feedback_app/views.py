from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import render, redirect

# Create your views here.
from feedback_app.forms import FeedbackForm
from feedback_app.models import Feedback


def submit_feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('feedback')
    else:
        form = FeedbackForm()
    return render(request, 'feedback_form.html', {'form': form})


def show_feedback(request):
    form = Feedback.objects.all()
    return render(request, "data_all.html", {'form': form})


def edit_feedback(request, pk):
    instance_edit = Feedback.objects.get(pk=pk)   # feedback models le ella objectneem ee variable lekk kond varunnu
    form = FeedbackForm(instance=instance_edit)   # edit button press aakkumbol athil ulla value aa form el kond varunnnu
    return render(request, 'feedback_form.html', {'form': form})


def delete_feedback(request, pk):
    instance = Feedback.objects.get(pk=pk)    # feedback models le ella objectneem ee variable lekk kond varunnu
    instance.delete()   # athine delete cheyyunnu
    form = Feedback.objects.all()  # veendum desplay cheyyunnnu
    return render(request, 'data_all.html', {'form': form})


def sign_up(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('sign_in')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


def sign_in(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('show')
    else:
        form = AuthenticationForm()
    return render(request, 'signin.html', {'form': form})


def sign_out(request):
    logout(request)
    return redirect('signin')
