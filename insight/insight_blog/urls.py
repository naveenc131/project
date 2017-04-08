from django.conf.urls import url
from django.contrib.auth import views as auth_views
from insight_blog import views

#Our customised url patterns
urlpatterns = [ 
<<<<<<< HEAD
				url(r'^$', views.index, name='index'),
				
=======
				url(r'^$',views.index, name='index'),
				url(r'^login/$', auth_views.login,{'template_name': 'forms.html'}, name='login'),
				url(r'^logout/$', auth_views.logout, name='logout'),

>>>>>>> 2e5afefce48b72fed9629851cd046a391bef5076
				]
