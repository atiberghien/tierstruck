from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _

class TourMgmtConfig(AppConfig):
    name = 'tour_mgmt'
    verbose_name =  _("Gestionnaire de tournée")
