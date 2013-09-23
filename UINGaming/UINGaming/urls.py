from django.conf.urls import patterns, include, url
import src.home.views
import src.users.views
import src.events.views
import src.utils.api
# Uncomment the next two lines to enable the admin:

from django.contrib import admin
admin.autodiscover()

handler404 = 'mysite.views.my_custom_404_view'
urlpatterns = patterns('',
	# Examples:
	# url(r'^$', 'WebApp.views.home', name='home'),
	# url(r'^WebApp/', include('webapp.foo.urls')),
	
	# ############################ #
	# #######  INDEX URLS ######## #
	# ############################ #
	url(r'^$',src.utils.api.IndexRequestHandler),
	url(r'^register$',src.utils.api.IndexRequestHandler),
	url(r'^signin$',src.utils.api.IndexRequestHandler),
	url(r'^home$',src.utils.api.IndexRequestHandler),
	url(r'^events$',src.utils.api.IndexRequestHandler),
	url(r'^eventregister$',src.utils.api.IndexRequestHandler),
	url(r'^events/event/[0-9]+$',src.utils.api.IndexRequestHandler),
	#url(r'^passwd_recover/(?P<username>[a-zA-Z0-9_-]{3,20}$)$',src.users.views.PasswordRecoverFormView),
	
	
	
	
	# Uncomment the admin/doc line below to enable admin documentation:
	# url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
	
	# Uncomment the next line to enable the admin:
	url(r'^admin/', include(admin.site.urls)),
	
	
	# ############################ #
	# ######### API URLS ######### #
	# ############################ #
	url(r'^api/signup$',src.users.views.SignUpAPI),
	url(r'^api/signin$',src.users.views.SignInAPI),
	url(r'^api/password_recover$',src.users.views.PasswordRecoverAPI),
	url(r'^api/password_recover_reset$',src.users.views.PasswordRecoverResetAPI),
	url(r'^api/password_recover/(?P<username>[a-zA-Z0-9_-]{3,20}$)$',src.users.views.PasswordRecoverFormAPI),
	url(r'^api/logout$',src.users.views.LogOutAPI),
	url(r'^api/events$',src.events.views.EventsAPI),
	url(r'^api/eventMembership$',src.events.views.EventMembershipAPI),
	# FOR TESTING FRONTEND
	url(r'^api/slides$',src.home.views.SlidesAPI),
	url(r'^api/features$',src.home.views.FeaturesAPI),
	
	# ############################ #
	# ####### PARTIALS URLS ###### #
	# ############################ #
	url(r'^partials/(?P<page>[a-zA-Z]*$)',src.utils.api.PartialsRequestHandler),
	
	# PERMALINKS#    
	url(r'^events/(?P<pk>[a-zA-Z]*$)',src.utils.api.IndexRequestHandler),
)
