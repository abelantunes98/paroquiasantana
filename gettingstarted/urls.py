from django.conf.urls import include, url
from django.urls import path

from django.contrib import admin
admin.autodiscover()

import hello.views

# Examples:
# url(r'^$', 'gettingstarted.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    path('', hello.views.index, name='index'),
    url(r'index', hello.views.index, name='index'),
    url(r'^news', hello.views.news, name='news'),
    path('admin/', admin.site.urls),
]
