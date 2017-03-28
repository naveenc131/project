from django.conf.urls import url
from . import views

#Our customised url patterns
urlpatterns = [ 
				url(r'^$', views.index, name='index'),
				url(r'^login/', views.login_view,name="login"),
    			url(r'^register/', views.register_view,name="register"),
				]
