from django.db import models

# Create your models here.

class SurveyResult(models.Model):
  username = models.CharField(max_length=255)
  responses = models.TextField()
  created_on = models.DateTimeField(auto_now_add=True)