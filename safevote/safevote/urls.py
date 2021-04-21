"""safevote URL Configuration

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
from django.conf.urls import url, include 
from django.contrib import admin
from safevote_app import views
from django.urls import path 

urlpatterns = [
    path('', views.index, name='index'),
    path('addvote/<slug:election_id>/<slug:user_id>/<slug:vote>/<slug:hmac>', views.AddVote),
    path('addelection/<slug:election_id>/<slug:candidates>/<slug:hmac>', views.AddElection),
    path('calculateelection/<slug:election_id>/<slug:hmac>', views.CalculateElection),
    path('deleteelection/<slug:election_id>/<slug:hmac>', views.DeleteElection),
    path('testdb', views.TestDB)
]
