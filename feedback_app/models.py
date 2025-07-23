from django.db import models

# Create your models here.


class Feedback(models.Model):
    name = models.CharField(max_length=15)
    email = models.EmailField(max_length=25)
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)
