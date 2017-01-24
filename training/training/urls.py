from django.conf.urls import include, url
from django.contrib import admin

from tplatform import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^browse/strategy', views.strategy, name='browse.strategy'),
	url(r'^browse/filter/category=(?P<category>(\w+&)*\w*)/tags=(?P<tags>(\d+&)*\d*)/', views.filter_detail, name='browse.filter_detail'),
	url(r'^browse/content', views.content, name='browse.content'),
	url(r'^browse/misc', views.misc, name='browse.misc'),
	url(r'^browse/', views.browse, name='browse'),
	url(r'^about/', views.about, name='about'),
	url(r'^article/(?P<id>\d+)/', views.article_detail, name='browse.article_detail'),
    url(r'^admin/', include(admin.site.urls)),
]
