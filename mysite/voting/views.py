from django.shortcuts import render, redirect
from account.models import Account
from django.http import HttpResponse
# Create your views here.

def voting_screen_view(request):
    # if not request.user.is_authenticated:
    #     return redirect('register')
    # context={}

    # accounts = Account.objects.all()
    # context['accounts'] = accounts


    return render(request, 'voting/voting.html')
