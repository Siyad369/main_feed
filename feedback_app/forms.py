from django import forms
from .models import Feedback


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Your name', 'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Your email', 'class': 'form-control'}),
            'message': forms.Textarea(attrs={'placeholder': 'Your feedback', 'class': 'form-control', 'rows': 4}),
        }
