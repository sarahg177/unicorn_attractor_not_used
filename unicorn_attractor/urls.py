"""unicorn_attractor URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from home.views import home
from bugs.views import get_bugs_list, create_a_new_bug, view_bug_details, edit_an_item
from features.views import get_features_list
from accounts.views import login, logout, registration

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home, name="home"),
    url(r'^accounts/logout/$', logout, name="logout"),
    url(r'^accounts/login/$', login, name="login"),
    url(r'^accounts/register/$', registration, name="registration"),
    url(r'^bugs$', get_bugs_list, name="bugs"),
    url(r'^features$', get_features_list, name="features"),
    url(r'^add$', create_a_new_bug, name="add"),
    url(r'^edit/(?P<id>\d+)$', edit_an_item),
    url(r'^bug_details', view_bug_details, name="bug_details"),
]
