from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import generic
from .models import SurveyResult

# Create your views here.
class IndexView(generic.ListView):
  template_name = 'survey_results/index.html'

  def get_queryset(self):
    return SurveyResult.objects.all()