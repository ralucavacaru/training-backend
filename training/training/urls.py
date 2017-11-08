from django.conf.urls import include, url
from django.contrib import admin

from tplatform import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^browse/filter/category=(?P<category>(\w+&)*\w*)/tags=(?P<tags>(\d+&)*\d*)/types=(?P<types>(\d+&)*\d*)/authors=(?P<authors>(\d+&)*\d*)/', views.filter_detail, name='browse.filter_detail'),
	url(r'^trainers/', views.trainers, name='trainers'),
	url(r'^article/(?P<id>\d+)/', views.article_detail, name='browse.article_detail'),
	url(r'^trainer/(?P<id>\d+)/', views.trainer_detail, name='trainers.trainer_detail'),
	url(r'^contact/request_training', views.request_training, name='contact.request_training'),
	url(r'^contact/request_resources', views.request_resources, name='contact.request_resources'),
	url(r'^contact/send_feedback', views.send_feedback, name='contact.send_feedback'),
	url(r'^contact/join_team', views.join_team, name='contact.join_team'),
	url(r'^contact/', views.contact, name='contact'),
    url(r'^admin/', include(admin.site.urls)),
]
