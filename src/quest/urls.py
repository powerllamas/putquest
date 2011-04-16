from django.conf.urls.defaults import *
from quest.views import IndexView

urlpatterns = patterns('',
    (r'^$', IndexView.as_view()),
)
