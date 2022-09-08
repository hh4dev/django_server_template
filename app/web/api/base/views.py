# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import json
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.generic.base import View


class APIView(View):

    def dispatch(self, request, *args, **kwargs):
        """
        リクエストの事前処理
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        return super(APIView, self).dispatch(request, *args, **kwargs)

    def render_to_response(self, context, *args, **kwargs):
        """
        JSON形式で返す
        :param context: dict
        :param args: tuple
        :param kwargs: dict
        :return: JsonResponse
        """
        # return JsonResponse(context)
        return HttpResponse(
            json.dumps(context, ensure_ascii=False)
        )
