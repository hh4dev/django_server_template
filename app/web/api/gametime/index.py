# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.utils.six import text_type

from app.web.api.base.views import APIView
from app.support.gametime import Gametime


class IndexView(APIView):

    def get(self, _request, *args, **kwargs):
        """
        ゲーム内時刻を返す
        :param _request:
        :param args: tuple
        :param kwargs: dict
        :return: dict
        """
        now = Gametime.now()

        return self.render_to_response({
            'now': text_type(now),
        })
