from django.conf.urls import include, url
from django.contrib import admin

from tplatform import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^browse/strategy', views.strategy, name='strategy'),
	url(r'^browse/content', views.content, name='content'),
	url(r'^browse/misc', views.misc, name='misc'),
	url(r'^browse/', views.browse, name='browse'),
	url(r'^about/', views.about, name='about'),
	url(r'^article/(?P<id>\d+)/', views.article_detail, name='article_detail'),
    url(r'^admin/', include(admin.site.urls)),
]
