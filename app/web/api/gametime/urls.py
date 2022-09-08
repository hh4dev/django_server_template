# -*- coding: utf-8 -*-
from django.urls import path, re_path, include

from .index import IndexView


urlpatterns = (
    re_path(r'^/get$', IndexView.as_view(), name='gametime_get'),
)
