from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^api/energy$', views.energy_list),
	url(r'^api/energy/(?P<pk>[0-9]+)$', views.energy_detail),
	url(r'^api/energy/published$', views.energy_list_published)
]