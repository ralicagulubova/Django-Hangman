from django.conf.urls import patterns, include, url

from hangmanGame.game.views
#from django.contrib import admin
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^login/$', 'hangman.views.login'),
    # url(r'^logout/$', 'hangman.views.logout'),
    # url(r'^register/$', 'hangman.views.register'),
    # url(r'^register_success/$', 'hangman.views.register_success'),
    #url(r'^create_game/$', create_game, name='create-game'),
    #url(r'^success_create/$', success_create, name='success-create'),
    #url(r'^$', 'hangman.views.PlayersNames', name='names'),
    # url(r'^hangmanGame/', include('hangmanGame.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #url(r'^admin/', include(admin.site.urls)),
)