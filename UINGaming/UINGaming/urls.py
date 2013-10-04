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
	url(r'^profile$',src.utils.api.IndexRequestHandler),
	url(r'^eventAdd$',src.utils.api.IndexRequestHandler),
	url(r'^eventEdit$',src.utils.api.IndexRequestHandler),
	url(r'^eventregister$',src.utils.api.IndexRequestHandler),
	url(r'^events/[0-9]+$',src.utils.api.IndexRequestHandler),
	url(r'^news$',src.utils.api.IndexRequestHandler),
	url(r'^news/add$',src.utils.api.IndexRequestHandler),
	url(r'^news/edit/[0-9]+$',src.utils.api.IndexRequestHandler),
	url(r'^news/[0-9]+$',src.utils.api.IndexRequestHandler),
	
	
	
	
	# Uncomment the admin/doc line below to enable admin documentation:
	# url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
	
	# Uncomment the next line to enable the admin:
	url(r'^admin/', include(admin.site.urls)),
	
	
	# ############################ #
	# ######### API URLS ######### #
	# ############################ #
	url(r'^api/user-session$',src.users.views.SessionInfoApi),
	url(r'^api/users$',src.users.views.UserProfileAPI),
	url(r'^api/users/(?P<username>[a-zA-Z0-9_-]{3,20}$)$',src.users.views.UserProfileAPI),
	url(r'^api/signup$',src.users.views.SignUpAPI),
	url(r'^api/signin$',src.users.views.SignInAPI),
	url(r'^api/password_recover$',src.users.views.PasswordRecoverAPI),
	url(r'^api/password_recover_reset$',src.users.views.PasswordRecoverResetAPI),
	url(r'^api/password_recover/(?P<username>[a-zA-Z0-9_-]{3,20}$)$',src.users.views.PasswordRecoverFormAPI),
	url(r'^api/logout$',src.users.views.LogOutAPI),
	url(r'^api/events$',src.events.views.EventsAPI),
	url(r'^api/eventsByUser$',src.events.views.EventsByUserAPI),
	url(r'^api/eventDelete$',src.events.views.EventDeleteAPI),
	url(r'^api/eventMembership$',src.events.views.EventMembershipAPI),
	url(r'^api/slides$',src.home.views.SlidesAPI),
	url(r'^api/features$',src.home.views.FeaturesAPI),
	url(r'^api/news$',src.home.views.NewsAPI),
	url(r'^api/news-viewer$',src.home.views.NewsViewerAPI),
        url(r'^api/news-delete$',src.home.views.NewsDeleteAPI),
	
	# ############################ #
	# ####### PARTIALS URLS ###### #
	# ############################ #
	url(r'^partials/(?P<page>[a-zA-Z]*$)',src.utils.api.PartialsRequestHandler),
)
