from django.contrib.auth.models import User
from django.core.management.base import BaseCommand, CommandError
from profiles.utils import get_unique_username

class Command(BaseCommand):
    help = 'Convert usernames to the correct format'

    def handle(self, *args, **options):
        """
        Usernames
        """
        users = User.objects.all()
        for user in users:
            user.username = get_unique_username(user.first_name, user.last_name)
            print u'%s %s >> %s' % (user.first_name, user.last_name, user.username)
            user.save()