from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^registration', views.registration),
    url(r'^login', views.login),
    url(r'^success', views.success),
    url(r'^delete', views.delete)
    # url(r'^(?P<number>\d+)$', views.show),
    # url(r'^(?P<number>\d+)$/edit', views.edit),
    # url(r'^(?P<number>\d+)$/delete', views.destroy),
    # url(r'^create$', views.create)
]
