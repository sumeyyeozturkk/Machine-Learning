from django.conf.urls import url, include 
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
	url(r'tahmin/(?P<metreKare>\d+(\.\d+)?)/(?P<odaSayisi>\d+(\.\d+)?)/$',views.EvFiyatTahmin.as_view()),
	url(r'.*/$',views.Hata.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)