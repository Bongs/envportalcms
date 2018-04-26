from django.db import models

# Create your models here.
from cms.models import CMSPlugin
from polls.models import Poll


class PollPluginModel(CMSPlugin):
  poll = models.ForeignKey(Poll)

  def __str__(self): # use __unicode__() if you are using Python 2
    return self.poll.question