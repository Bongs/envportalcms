from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from polls_cms_integration.models import PollPluginModel
from django.utils.translation import ugettext as _
# from cms.app_base import CMSApp
# from cms.apphook_pool import apphook_pool
# from django.conf.urls import url
# from polls.views import IndexView, DetailView

class PollPluginPublisher(CMSPluginBase):
  model = PollPluginModel  # model where plugin data are saved
  module = _("Polls")
  name = _("Poll Plugin")  # name of the plugin in the interface
  render_template = "polls_cms_integration/poll_plugin.html"

  def render(self, context, instance, placeholder):
    context.update({'instance': instance})
    return context

plugin_pool.register_plugin(PollPluginPublisher)  # register the plugin

# @apphook_pool.register  # register the application
# class PollsApphook(CMSApp):
#   app_name = "polls"
#   name = _("Polls Application")

#   def get_urls(self, page=None, language=None, **kwargs):
#     # return ["polls.urls"]
#     return [
#       url(r'^$', IndexView.as_view()),
#       url(r'^(?P<slug>[\w-]+)/?$', DetailView.as_view()),
#     ]
