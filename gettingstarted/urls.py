from django.conf.urls import include, url

from django.contrib import admin
from django.contrib.auth import views as auth_views
admin.autodiscover()

import hello.views

# Examples:
# url(r'^$', 'gettingstarted.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    url(r'^$', hello.views.home, name='home'),
    url(r'^settings/$', hello.views.settings, name='settings'),
    url(r'^settings/password/$', hello.views.password, name='password'),
    url(r'^signup/$', hello.views.signup, name='signup'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^oauth/', include('social_django.urls', namespace='social')),  # <--
    url(r'^admin/', admin.site.urls),
    url(r'^mail$', hello.views.spikeGmail, name='mail'),

    #Dashboard
    url(r'^dashboard/$', hello.views.dashboard, name='dashboard'),
    url(r'^dashboard_ejecutivo/$', hello.views.dashboard_ejecutivo, name='dashboard_ejecutivo'),
    url(r'^dashboard_ejecutivo/single$', hello.views.dashboard_ejecutivo_single, name='dashboard_ejecutivo_single'),
]