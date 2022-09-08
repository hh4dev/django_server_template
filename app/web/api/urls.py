# -*- coding: utf-8 -*-
from django.urls import path, re_path, include


_URLS_MODULE = __package__ + '.{}.urls'

urlpatterns = (
    re_path(r'^gametime', include(_URLS_MODULE.format('gametime'))),
)
