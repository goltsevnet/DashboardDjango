from django.core.management.base import BaseCommand
from dashboards.management.commands.generate.generate import start_gen


class Command(BaseCommand):
    def handle(self, *args, **options):
        return start()


person_count = 1000
multiplex = person_count / 10


def start():
    start_gen(users=1000, items=1000)
