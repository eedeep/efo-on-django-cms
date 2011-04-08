from django.contrib.auth.models import User
from django.utils.safestring import mark_safe
import re

def capfirst(value):
    """Capitalizes the first character of the value."""
    return value and value[0].upper() + value[1:]

def slugify(value):
    """
    Custom slugify that doesn't convert to lowercase
    """
    import unicodedata
    value = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore')
    value = unicode(re.sub('[^\w\s-]', '', value).strip())
    return mark_safe(re.sub('[-\s]+', '-', value))

def SlugifyUniquely(value, model, slugfield="slug"):
    """
    Custom SlugifyUniquely that uses slugify, that doesn't convert to lowercase
    """
    suffix = 0
    potential = base = slugify(value)
    while True:
        if suffix:
            potential = "-".join([base, str(suffix)])
        if not model.objects.filter(**{slugfield: potential}).count():
            return potential
        # we hit a conflicting slug, so bump the suffix & try again
        suffix += 1

def get_unique_username(first_name, last_name):
    """
    Returns a unique username based on the given first and last names. 
    Defined here as a util since it is called from multiple locations.
    """
    full_name = unicode(capfirst(last_name) + '-' + capfirst(first_name))
    return SlugifyUniquely(full_name, User, 'username')

