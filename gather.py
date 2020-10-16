import os
import pytumblr
import pickle

def get_client():
    consumer_key = os.getenv("TUMBLR_CONSUMER_KEY")
    consumer_secret = os.getenv("TUMBLR_CONSUMER_SECRET")
    oauth_token = os.getenv("TUMBLR_OAUTH_TOKEN")
    oauth_secret = os.getenv("TUMBLR_OAUTH_SECRET")
    client = pytumblr.TumblrRestClient(consumer_key, consumer_secret, oauth_token, oauth_secret)
    return client

def gather(client):
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
    except:
        with open('dailyposts.pickle', 'wb') as data:
            pickle.dump(posts, data)

def main():
    client = get_client()
    gather(client)

if __name__ == '__main__':
    main()