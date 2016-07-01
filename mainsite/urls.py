from django.conf.urls import include,url,patterns
from . import views
import django.contrib.auth.views as auth_views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^about-us/$', views.about_us, name='about_us'),
	url(r'^members/$', views.members, name='members'),
	url(r'^achievements/$', views.achievements, name='achievements'),
	url(r'^projects/$', views.our_projects, name='our_projects'),
	url(r'^tutorials/$', views.tutorials, name='tutorials'),
	url(r'^support-us/$', views.support_us, name='support_us'),
	url(r'^members/alumni/$', views.alumni, name='alumni'),
	url(r'^members/active/$', views.active_members, name='active_members'),
	url(r'^projects/ongoing/$', views.ongoing_projects, name='ongoing_projects'),
	url(r'^projects/completed/$', views.completed_projects, name='completed_projects'),
    url(r'^login/',auth_views.login, name="auth_views.login"),
    url(r'^home/', views.index, name='index'),
    url(r'^logout/$', views.logout_page),
	url(r'^accounts/login/$',auth_views.login, name="auth_views.login"),
	url(r'^accounts/userprofile/$', views.userprofile, name='userprofile'),
    url(r'^register/$', views.register),
    url(r'^profile/$', views.userprofile, name='userprofile'),
    url(r'^profile/edit/$', views.editprofile, name='editprofile'),
    url(r'^profile/addproject/$', views.addproject, name='addproject'),
    url(r'^profile/editproject/(?P<proj>)/$', views.editproject, name='editproject'),
    url(r'^register/success/$', views.success, name='success'),
    url(r'^register/fill_info/$', views.fill_info, name='fill_info'),
    url(r'^expo/$', views.expo, name='expo'),
]
