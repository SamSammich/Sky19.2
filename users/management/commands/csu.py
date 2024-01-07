from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create(
            email='admin@choko.com',
            first_name='Admin',
            last_name='Choko',
            is_staff=True,
            is_superuser=True
        )

        user.set_password('choko55')
        user.save()
