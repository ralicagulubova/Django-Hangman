from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib import auth
from game.models import Game, Profile
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
import hangman.views
from django.db.models import Q
#import game.hanggame




def create_game(request):
    user = auth.get_user(request)
    if user and Profile.objects.filter(user=user).count(): #and  not user.profile.create_game:    
        print request.method
        if request.method == 'POST':
            user.profile.play_game = False
            user.profile.create_game = True
            user.profile.finished_game = False
            user.profile.wined_game = False
            user.profile.lost_game = False
            user.profile.save()
            game = Game(created_by_id = user.id,  word = request.POST.get('word'), description = request.POST.get('description'),)
            game.save()
            return render_to_response('create_game.html', {
                'word' : game.word,
                'description' : game.description,
                },RequestContext(request))
        else:
            return render(request, 'create_game.html')

    else:
        return HttpResponseRedirect('/logout/')


def game_list(request):
    user = auth.get_user(request)
    if user and Profile.objects.filter(user=user).count():
        if request.method == 'GET':
            user.profile.play_game = True
            user.profile.create_game = False
            user.profile.finished_game = False
            user.profile.wined_game = False
            user.profile.lost_game = False
            user.profile.save()
            words = Game.objects.filter(~Q(word='') & ~Q(created_by_id = user.id)) 
            return render_to_response('game_list.html', {
                'words' : words,
                },RequestContext(request))
        else:
            return render(request, 'game_list.html')

    else:
        return HttpResponseRedirect('/logout/')





