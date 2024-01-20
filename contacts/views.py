from django.shortcuts import render, redirect
from .models import Contact
# Create your views here.

def contacts_screen_view(request):
    context = {}
    contacts = Contact.objects.all()
    context["contact"] = contacts
    searched = request.GET.get("q", "default")
    print(searched)
    searched_contacts = []
    for i in contacts:
        if str.lower(searched) in str.lower(i.contact_name):
            searched_contacts.append(i)
            context["contact"] = searched_contacts
    return render(request, 'contacts/contacts.html', context)

