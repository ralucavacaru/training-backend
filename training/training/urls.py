from django.conf.urls import include, url
from django.contrib import admin

from tplatform import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^browse/filter/category=(?P<category>(\w+&)*\w*)/tags=(?P<tags>(\d+&)*\d*)/types=(?P<types>(\d+&)*\d*)/authors=(?P<authors>(\d+&)*\d*)/', views.filter_detail, name='browse.filter_detail'),
	url(r'^trainers/', views.trainers, name='trainers'),
	url(r'^article/(?P<id>\d+)/', views.article_detail, name='browse.article_detail'),
	url(r'^trainer/(?P<id>\d+)/', views.trainer_detail, name='trainers.trainer_detail'),
	url(r'^contact/', views.contact, name='contact'),
    url(r'^admin/', include(admin.site.urls)),
]
