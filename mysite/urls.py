"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from personal.views import home_screen_view
from voting.views import voting_screen_view
from contacts.views import contacts_screen_view

from account.views import(
    registration_view,
    logout_view,
    login_view,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home_screen_view, name="home"),
    path('register/', registration_view, name="register"),
    path('logout/', logout_view, name="logout"),
    path('', login_view, name="login"),
    path('voting/', voting_screen_view, name="voting"),
    path('contacts/', contacts_screen_view, name="contacts"),
    path('verification/', include('verify_email.urls')),

]
