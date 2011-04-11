import re

from empcom.util.regex import in_admin_regex


class SatelliteUserMiddleware:
    """
    Provides a place for information from the request or session to
    be added to anything we need for the user front end
    """
    def process_request(self, request):
        """Currently sets the balance on the custom user object."""
        if not request.user.is_anonymous():
            if not re.match(in_admin_regex, request.path):
                request.user.balance.set(request) 

        
        # The following code has been left in as an example of how to
        # cache something on the request object
        #if not hasattr( request, 'cached_dictionary'):
        #    request.cached_dictionary = {}
        #    request.cached_dictionary.update(get_dict_function(request))

        return None
