from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _

class ProgrammesAppHook(CMSApp):
    name = _("Programmes App")
    urls = ["programmes.urls"]

apphook_pool.register(ProgrammesAppHook)
