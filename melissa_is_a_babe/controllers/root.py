# -*- coding: utf-8 -*-
"""Main Controller"""

from tg import expose, flash, require, url, request, redirect
from pylons.i18n import ugettext as _, lazy_ugettext as l_

from melissa_is_a_babe.lib.base import BaseController
from melissa_is_a_babe.model import DBSession, metadata
from melissa_is_a_babe.controllers.error import ErrorController

__all__ = ['RootController']

from tw2.protovis.custom import BubbleChart
import random

import itertools

import urllib
import simplejson
import itertools
import math

base_url = "http://ajax.googleapis.com/ajax/services/search/web?v=1.0"

def make_entry(combo):
    phrase = '"%s"' % " ".join(combo)
    print "Querying for %s." % phrase
    query = urllib.urlencode({ 'q': phrase })
    url = "%s&%s" % (base_url, query)
    results = urllib.urlopen(url)
    json = simplejson.loads(results.read())

    if 'estimatedResultCount' in json['responseData']['cursor']:
        count = int(json['responseData']['cursor']['estimatedResultCount'])
    else:
        count = len(json['responseData']['results'])

    value = math.log(count+1.000000001)

    return {
        'name' : "%s : %i " % (phrase, count),
        'value' : value,
        'text' : phrase[:10],
        'group' : len(combo),
    }

from multiprocessing import Pool
pool = Pool(processes=150)

class RootController(BaseController):
    """
    The root controller for the barcamp.roc.fall.2010 application.

    All the other controllers and WSGI applications should be mounted on this
    controller. For example::

        panel = ControlPanelController()
        another_app = AnotherWSGIApplication()

    Keep in mind that WSGI applications shouldn't be mounted directly: They
    must be wrapped around with :class:`tg.controllers.WSGIAppController`.

    """

    error = ErrorController()

    @expose('melissa_is_a_babe.templates.index')
    def index(self, sentence="word to your moms"):
        """Handle the front-page."""
        words = str(sentence).split()
        combos = []
        for i in range(len(words)):
            combos += list(itertools.combinations(words, i+1))

        data = pool.map(make_entry, combos)

        chart = BubbleChart(
            id='a-chart-for-my-friends',
            p_width=750,
            p_height=750,
            p_data=data
        )

        return dict(page='index', widget=chart)
