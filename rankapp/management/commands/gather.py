import os
import pytumblr
import pickle
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    def get_client(self):
        consumer_key = os.getenv("TUMBLR_CONSUMER_KEY")
        consumer_secret = os.getenv("TUMBLR_CONSUMER_SECRET")
        oauth_token = os.getenv("TUMBLR_OAUTH_TOKEN")
        oauth_secret = os.getenv("TUMBLR_OAUTH_SECRET")
        client = pytumblr.TumblrRestClient(consumer_key, consumer_secret, oauth_token, oauth_secret)
        return client


    def handle(self, *args, **options):
        client = self.get_client()
        # ダッシュボードから２０件分のポストを取得
        posts = client.dashboard()
        posts = posts['posts']

        # pickleで書き込み
        try:
            with open('dailyposts.pickle', 'rb') as data:
                dumped_data = pickle.load(data)
                dumped_data += posts
            with open('dailyposts.pickle', 'wb') as data:
                pickle.dump(dumped_data, data)
            self.stdout.write(self.style.SUCCESS('Successfully gathering Posts'))

        except:
            with open('dailyposts.pickle', 'wb') as data:
                pickle.dump(posts, data)
            self.stdout.write(self.style.SUCCESS('Unsuccessfully gathering Posts!!!!!'))
        