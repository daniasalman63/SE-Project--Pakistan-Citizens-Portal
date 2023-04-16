from django.shortcuts import render, redirect
from account.models import Account

# Create your views here.

def home_screen_view(request):
    if not request.user.is_authenticated:
        return redirect('login')
    context={}

    accounts = Account.objects.all()
    context['accounts'] = accounts


    return render(request, 'personal/home.html', context)
