from django.shortcuts import render, redirect
from .models import Candidate
# Create your views here.

def voting_screen_view(request):
    context = {}
    candidates = Candidate.objects.all()
    print(candidates)
    context["candidate"] = candidates
    if request.method == "post":
        voted_candidate = request.POST.get('candidate')
        print(type(voted_candidate))
        candi = Candidate.objects.get(candidate_name=voted_candidate)
        print(candi)
    return render(request, 'voting/voting.html', context)