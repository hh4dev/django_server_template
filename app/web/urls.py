# -*- coding: utf-8 -*-
from django.contrib import admin
from django.urls import path, re_path, include

urlpatterns = (
    re_path(r'^api/', include('app.web.api.urls')),
)
