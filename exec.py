from django.core.management.base import BaseCommand
from rankapp.models import PostModel
from . import ranking

class Command(BaseCommand):
    def handle