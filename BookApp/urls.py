from django.urls import path, re_path
from BookApp import views
from django.urls import re_path as url


urlpatterns=[
    url(r'^book$',views.bookApi),
    url(r'^book/([0-9]+)$',views.bookApi)
]