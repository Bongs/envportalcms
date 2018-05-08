from django.conf.urls import url
from . import views

# urlpatterns = patterns('',
#     url(r'^submit/$', 'cms_saq.views.submit', name='cms_saq_submit'),
#     url(r'^scores/$', 'cms_saq.views.scores', name='cms_saq_scores'),
#     url(r'^edit/$', 'cms_saq.views.change_answer_set', name='cms_saq_edit'),
# )

urlpatterns = [
    url(r'^submit/$', views.submit, name='cms_saq_submit'),
    url(r'^scores/$', views.scores, name='cms_saq_scores'),
    url(r'^edit/$', views.change_answer_set, name='cms_saq_edit'),
]