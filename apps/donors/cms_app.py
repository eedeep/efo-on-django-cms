from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _

class DonorsAppHook(CMSApp):
    name = _("Donors App")
    urls = ["donors.urls"]

apphook_pool.register(DonorsAppHook)
