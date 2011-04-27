from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _

class PeopleAppHook(CMSApp):
    name = _("People App")
    urls = ["people.urls"]

apphook_pool.register(PeopleAppHook)
