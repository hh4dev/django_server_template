# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from datetime import datetime, timezone, timedelta


class Gametime():

    @classmethod
    def now(cls):
        """
        rtype: datetime
        """
        tz = timezone(timedelta(hours=+9), 'JST')
        return datetime.now(tz)
