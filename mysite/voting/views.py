from django.shortcuts import render, redirect
from account.models import Account
from django.http import HttpResponse
from .models import Candidate
# Create your views here.

def voting_screen_view(request):
    # if not request.user.is_authenticated:
    #     return redirect('register')
    # context={}

    # accounts = Account.objects.all()
    # context['accounts'] = accounts
    context = {}
    # djtext = request.GET.get('text', 'default')
    # candidate = request.GET.get('candidate', 'off')
    # candidate2 = request.GET.get('candidate2', 'off')
    # if candidate == "on":
    #     print(djtext)
    #     print(candidate)
    #     params["Candidates"] = candidate
    #     print(params["Candidates"])
    # elif candidate2 == "on":
    #     print(candidate2)
    candidates = Candidate.objects.all()
    print(candidates)
    context["candidate"] = candidates
    # voted_candidate = request.POST.get('candidate', "off")
    # print(len(voted_candidate))
    # if len(voted_candidate) > 1:
    #     for i in voted_candidate:
    #         request.GET.get(i, "off")
    if request.POST:
        voted_candidate = request.POST.get('candidate', "off")
        print(voted_candidate)
        # candidate = Candidate.objects.filter(candidate_name = "")

    return render(request, '/voting/voting.html', context)
