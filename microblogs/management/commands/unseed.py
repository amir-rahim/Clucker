from django.core.management.base import BaseCommand, CommandError
from faker import Faker
from ...models import User

class Command(BaseCommand):
    def __init__(self):
        super().__init__()
        self.faker = Faker('en_GB')

    def handle(self, *args, **options):
        User.objects.filter(is_superuser=False).delete()