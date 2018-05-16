from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import generic
from .models import SurveyResult
import requests

# Create your views here.
class IndexView(generic.ListView):
  template_name = 'survey_results/index.html'

  resp = requests.get(
                      'https://api.surveymonkey.com/v3/surveys/151087553/responses/bulk',
                      headers={
                        'Authorization': 'bearer FPyltocM1VFRmUDLCFiuH3Q6t0XpdDcWxTqAatCAiX2x1lgi--Ox.shO-EZ6soEvVQUQg0PusykMEdtZc-PrjBZulEe-kP703Hz0Qjmby9izfAKYrHXWtjB4FlVC7OQX'
                      }
                    )
  print(resp.text)

  sr = SurveyResult(responses=resp.json()['data'])
  sr.save()


  def get_queryset(self):
    return SurveyResult.objects.all()
    # return resp