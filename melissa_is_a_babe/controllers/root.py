# -*- coding: utf-8 -*-
"""Main Controller"""

from tg import expose, flash, require, url, request, redirect
from pylons.i18n import ugettext as _, lazy_ugettext as l_

from melissa_is_a_babe.lib.base import BaseController
from melissa_is_a_babe.model import DBSession, metadata
from melissa_is_a_babe.controllers.error import ErrorController

__all__ = ['RootController']


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
    def index(self):
        """Handle the front-page."""
        return dict(page='index')
