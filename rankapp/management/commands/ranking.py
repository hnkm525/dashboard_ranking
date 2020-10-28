import os
import pickle
import json
import requests
from django.core.management.base import BaseCommand, CommandError
from rankapp.models import PostModel


class Command(BaseCommand):
    def get_posts(self):
        try:
            with open('dailyposts.pickle', 'rb') as data:
                posts = pickle.load(data)
        except:
            posts = None
        return posts

    def sort_posts(self, posts):
        # 重複の削除
        posts = list(map(json.loads, set(map(json.dumps, posts))))
        # 収集したpostsをnote_count順にソート
        sorted_posts = sorted(posts, key=lambda x:x['note_count'], reverse=True)

        # postのタイプをtext, photoで分離
        text_posts = []
        media_posts = []
        for post in sorted_posts:
            if post['type'] == 'text':
                text_posts.append(post)
            elif post['type'] == 'photo':
                media_posts.append(post)
            else:
                pass
        return media_posts, text_posts

    def download_media(self, media_posts):
        for i, post in enumerate(media_posts):
            url = post['photos'][0]['original_size']['url']
            file_name = '/usr/share/nginx/html/media/' + url.split('/')[-1]
            response = requests.get(url)
            image = response.content
            with open(file_name, 'wb') as data:
                data.write(image)

    def gen_media_obj(self, media_posts):
        self.allok = True
        for post in media_posts:
            # 画像がダウンロードできているか確認
            if os.path.isfile('/usr/share/nginx/html/media/' + post['photos'][0]['original_size']['url'].split('/')[-1]):
                PostModel.objects.create(post_type = 'media',
                                         post_url = post['post_url'],
                                         note_count = post['note_count'],
                                         blog_name = post['blog_name'],
                                         blog_url = post['blog']['url'],
                                         title = 'title',
                                         body = 'body',
                                         caption = post['caption'],
                                         link = post['post_url'],
                                         images = post['photos'][0]['original_size']['url'].split('/')[-1],
                                         summary = post['summary']
                                        )
            else:
                self.allok = False
        if self.allok:
            self.stdout.write(self.style.SUCCESS('Successfully generating Posts'))
        else:
            self.stdout.write(self.style.SUCCESS('Failed generating Posts'))

    def handle(self, *args, **options):
        posts = self.get_posts()
        media_posts, text_posts = self.sort_posts(posts)
        self.download_media(media_posts)
        self.gen_media_obj(media_posts)
