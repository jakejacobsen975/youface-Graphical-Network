import time
import tinydb
import os
import openai
import uuid
# from dotenv import load_dotenv

def add_post(db, user, text, image):
    posts = db.table('posts')

    post_id = str(uuid.uuid4())

    posts.insert({'id': post_id,'user': user['username'], 'text': text, 'time': time.time(),'num_ratings': 0,'sum_ratings':0, 'comments': [], 'num_likes':0,"meme_image":image})


def get_posts(db, user):
    posts = db.table('posts')
    Post = tinydb.Query()
    user_posts = posts.search(Post.user == user['username'])

    for post in user_posts:
        if post['num_ratings'] > 0:
            post['avg_rating'] = post['sum_ratings'] / post['num_ratings']
        else:
            post['avg_rating'] = 0

    return user_posts

def rate_post(db, post_id, sum_rating):
    posts = db.table('posts')
    Post = tinydb.Query()
    record = posts.get(Post.id == post_id)
    print("this is post_id",post_id)
    print("this is record",record)
    record['sum_ratings'] = record.get('sum_ratings', 0) + sum_rating
    record['num_ratings'] += 1

    posts.update(record, Post.id == post_id)


def commentOnPost(db, post_id, text):
    posts = db.table('posts')
    Post = tinydb.Query()
    record = posts.get(Post.id == post_id)
    record['comments'].append(text)
    print("this comment value:", text)

    posts.update(record, Post.id == post_id)

def like_post(db, post_id):
    posts = db.table('posts')
    Post = tinydb.Query()
    record = posts.get(Post.id == post_id)
    record['num_likes'] += 1

    posts.update(record, Post.id == post_id)

def commentOnPost(db, post_id, text):
    posts = db.table('posts')
    Post = tinydb.Query()
    record = posts.get(Post.id == post_id)
    record['comments'].append(text)
    print("this comment value:", text)

    posts.update(record, Post.id == post_id)