from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _

class ContactAppHook(CMSApp):
    name = _("Contact App")
    urls = ["contact.urls"]

apphook_pool.register(ContactAppHook)
