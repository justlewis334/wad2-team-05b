import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'poemgram.settings')

import django
django.setup()

from django.contrib.auth.models import User
from poemApp.models import UserProfile, Poem, Like, Comment


def populate():
    users = [
        {'user': 'test',
         'password': 'password'},
        {'user': 'test1',
         'password': 'password'},
        {'user': 'test2',
         'password': 'password'},
        {'user': 'test3',
         'password': 'password'},
        {'user': 'test4',
         'password': 'password'},
        {'user': 'test5',
         'password': 'password'},
        {'user': 'test6',
         'password': 'password'},
        {'user': 'test7',
         'password': 'password'},
    ]

    poems = [
        {'title': 'poem1',
         'articletitle': 'title1',
         'text': 'text1'},
        {'title': 'poem2',
         'articletitle': 'title2',
         'text': 'text2'},
        {'title': 'poem3',
         'articletitle': 'title3',
         'text': 'text3'},
        {'title': 'poem12',
         'articletitle': 'title12',
         'text': 'text12'},
        {'title': 'poem14',
         'articletitle': 'title31',
         'text': 'text1'},
        {'title': 'poem11',
         'articletitle': 'title125',
         'text': 'text1'},

    ]

    comments = [
        {}
    ]

    user_profs = []
    poem_objs = []

    for user in users:
        u = add_user(user['user'], user['password'])
        user_profs.append(u)

    i = 0
    for poem in poems:
        p = add_poem(poem['title'], user_profs[i], poem['articletitle'], poem['text'])
        poem_objs.append(p)
        i += 1

    # for comment in comments:
    #     add_comment()


def add_user(user, password='password', email='e@mail.com'):
    u = User.objects.get_or_create(username=user, password=password)[0]
    u.email = email
    u.save()
    return u


def add_poem(title, user, articletitle, text, url='https://www.google.com'):
    p = Poem.objects.get_or_create(title=title)[0]
    p.user = user
    p.articleTitle = articletitle
    p.text = text
    p.url = url
    p.save()
    return p


if __name__ == '__main__':
    print('Starting DB population script...')
    populate()
