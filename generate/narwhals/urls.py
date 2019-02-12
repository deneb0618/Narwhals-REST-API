from django.conf.urls import patterns, url, include
from rest_framework import routers

from views import *

router = routers.DefaultRouter()
router.register(r'accounts', UserView, 'list')

urlpatterns = patterns(
    '',
    url(r'^narwhals/', include(router.urls)),
    url(r'^entrenamientos/$', EntrenamientoList.as_view()),
    url(r'^entrenamientos/(?P<pk>[0-9]+)/$', EntrenamientoDetail.as_view()),
)
