from files.views import FileViewSet
from rest_framework.routers import SimpleRouter 
from django.conf.urls import patterns, include, url
from django.contrib import admin

router = SimpleRouter()
router.register(r'files', FileViewSet)

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(router.urls))
)
