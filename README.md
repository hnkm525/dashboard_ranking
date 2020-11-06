# dashboard_ranking
dashboard_ranking makes your Tumblr dashboard's daily ranking.  

## Overview
Tumblrダッシュボードからライク・リブログの合計数が多いポスト順に抽出してランキング形式で表示する．  
[Ex.](http://lime-sandwich.com/photo)

## Description
現状対応しているポストの形態は画像ポストのみです．

## Requirement
- Python 3.6.9
- Django 3.1.2
- PyTumblr 0.1.0
- Pillow
  
## Usage
### 初期設定
ダッシュボードの情報を取得するためにTumblr APIを用いています．登録をしていない方は[ここ](https://www.tumblr.com/login?redirect_to=%2Foauth%2Fapps)からアプリケーションの登録をしてください．
環境変数にTUMBLR_CONSUMER_KEY, TUMBLR_CONSUMER_SECRET, TUMBLR_OAUTH_TOKEN, TUMBLR_OAUTH_SECRETを登録してください  
### ダッシュボードの取得
```
$ python3 manage.py gather
```
Tumblr APIのレート制限に引っかからないような頻度で実行する
2020/11/06現在のTumblr API Rate Limitsは以下の通りに定められている．  
- 1,000 API calls per hour, per consumer key.  
- 5,000 API calls per day, per consumer key.  

### ランキングの更新
```
$ python3 manage.py ranking
```

### ポストデータベースの削除
```
$ python3 manage.py delete
```

## Author
[hnkm525](https://github.com/hnkm525 "")
