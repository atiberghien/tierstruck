# -*- coding: utf-8 -*-

from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _

class TourMgmtApphook(CMSApp):
    name = _("Gestionnaire de tournee")
    _urls = ["tour_mgmt.urls"]

apphook_pool.register(TourMgmtApphook)
