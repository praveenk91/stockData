from django.conf.urls import url
from django.contrib import admin
from mysite.views import hello, index

stock = ["Reliance", "3MIndia"]

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^hello/$', hello),
    url(r'^stock/$', index),
]