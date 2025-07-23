from django.db import models

# Create your models here.


class Feedback(models.Model):
    name = models.CharField(max_length=15)
    email = models.EmailField()
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)
