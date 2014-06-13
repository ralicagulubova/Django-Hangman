from django.conf.urls import patterns, include, url
from django.contrib import admin
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
#import game.views
urlpatterns = patterns('',
    # Examples:
    #url(r'^game/', include('game.urls')),
    url(r'^game/create_game/$', 'game.views.create_game', name = 'create-game'),
    url(r'^game/game_list/$', 'game.views.game_list', name = 'game-list'),
    #url(r'^game/success_create/$', 'game.views.success_create', name = 'success-create'),
    url(r'^login/$', 'hangman.views.login', name = 'login'),
    url(r'^logout/$', 'hangman.views.logout'),
    url(r'^register/$', 'hangman.views.register', name = 'register'),
    url(r'^register_success/$', 'hangman.views.register_success'),

    #url(r'^game/create_game/$', 'game.views.create_game'),
    #url(r'^create_game/$', 'game.views.create_game'),
    #url(r'^$', 'hangman.views.PlayersNames', name='names'),
    # url(r'^hangmanGame/', include('hangmanGame.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #url(r'^admin/', include(admin.site.urls)),
)
