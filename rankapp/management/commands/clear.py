import os
import pathlib
from rankapp.models import PostModel
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    def handle(self, *args, **options):
        try:
            #前日分の投稿の削除
            PostModel.objects.all().delete()
            #dashboardの投稿を集めたdailiposts.pickleの初期化
            os.remove('dailyposts.pickle')
            f = pathlib.Path('dailyposts.pickle')
            f.touch()
            self.stdout.write(self.style.SUCCESS('Successfully initiate'))
        except:
            self.stdout.write(self.style.SUCCESS('Unsuccessfully initiate!!!!!'))
        