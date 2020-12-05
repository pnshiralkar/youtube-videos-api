import asyncio
import os

from django.core.management import call_command
from django.core.management.commands.runserver import Command as BaseCommand

loop = asyncio.get_event_loop()


def start_sync():
    print("Starting Sync with Youtube...")
    call_command('sync_with_youtube')


class Command(BaseCommand):
    """Django command to runserver and
    also sync the DB with youtube API at specific interval asynchronously"""

    def handle(self, *args, **options):
        if os.environ.get('RUN_MAIN') != 'true':
            loop.run_in_executor(None, start_sync)
        super(Command, self).handle(*args, **options)
