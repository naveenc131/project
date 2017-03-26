from django.conf.urls import url
from . import views

#Our customised url patterns
urlpatterns = [ 
				url(r'^$', views.index, name='index'),
				]
