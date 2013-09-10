from django.conf.urls import patterns, include, url
import src.home.views
import src.authentication.views
# Uncomment the next two lines to enable the admin:

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'WebApp.views.home', name='home'),
    # url(r'^WebApp/', include('webapp.foo.urls')),
    
    # ############################ #
    # ########  HTML URLS ######## #
    # ############################ #
    url(r'^$',src.home.views.HomeView),
    url(r'^signup$',src.authentication.views.SignUpView),
    url(r'^signin$',src.authentication.views.SignInView),
    url(r'^logout$',src.authentication.views.LogOutView),
    url(r'^passwd_recover$',src.authentication.views.PasswordRecoverView),
    url(r'^passwd_recover/(?P<username>[a-zA-Z0-9_-]{3,20}$)$',src.authentication.views.PasswordRecoverFormView),
    
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    
    
    # ############################ #
    # ######### API URLS ######### #
    # ############################ #
    url(r'^api/signup$',src.authentication.views.SignUpAPI),
    url(r'^api/signin$',src.authentication.views.SignInAPI),
)
