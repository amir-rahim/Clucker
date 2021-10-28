from django.core.management.base import BaseCommand, CommandError
from faker import Faker
from ...models import User


class Command(BaseCommand):
    def __init__(self):
        super().__init__()
        self.faker = Faker('en_GB')

    def handle(self, *args, **options):
        for i in range(0, 500):
            User.objects.create_user(username='@' + self.faker.user_name(),
                                     first_name=self.faker.first_name(),
                                     last_name=self.faker.last_name(),
                                     email=self.faker.ascii_safe_email(),
                                     bio=self.faker.paragraph(nb_sentences=3, variable_nb_sentences=True))
