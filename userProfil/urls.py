from django.conf.urls import url

from . import views


urlpatterns = [
	 url(r'^change_password/$', views.change_password, name='change_password'),
	 url(r'^change_mail/$', views.change_mail, name='change_mail'),
	 url(r'^change_pseudo/$', views.change_pseudo, name='change_pseudo'),
]
app_name = 'userProfil'