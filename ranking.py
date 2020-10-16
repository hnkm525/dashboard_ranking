import pickle
import json
import pprint
import requests
import cv2
#from rankapp.models import models

def get_posts():
    try:
        with open('dailyposts.pickle', 'rb') as data:
            posts = pickle.load(data)
    except:
        posts = None
    return posts

def sort_posts():
    posts = get_posts()
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

def gen_media_obj(media_posts):
    for i, post in enumerate(media_posts):
        url = post['photos'][0]['original_size']['url']
        file_name = './images/' + url.split('/')[-1]
        response = requests.get(url)
        image = response.content

        with open(file_name, 'wb') as data:
            data.write(image)

def test(media_posts):
    for i, post in enumerate(media_posts):
        url = post['photos'][0]['original_size']['url']
        file_name = './images/' + url.split('/')[-1]
        response = requests.get(url)
        image = response.content
        with open(file_name, 'wb') as data:
            data.write(image)
        if file_name == './images/1821483c1a5ca4bd49516b49b8777893bf3e9749.jpg':
            pprint.pprint(post)
        if file_name == './images/605519588982638f2693e2d65e78596bb830ac4b.jpg':
            pprint.pprint(post)
            
        print(file_name)

    print(len(media_posts))

def main():
    media_posts, text_posts = sort_posts()
    #gen_media_obj(media_posts)    
    test(media_posts)    
    


main()