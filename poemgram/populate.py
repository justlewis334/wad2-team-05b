import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'poemgram.settings')

import django
django.setup()

from poemApp.models import UserProfile, Poem, Like, Comment


def populate():
    users = [
        {'user': 'test'},
        {'user': 'test1'},
        {'user': 'test2'},
        {'user': 'test3'},
        {'user': 'test4'},
        {'user': 'test5'},
        {'user': 'test6'},
        {'user': 'test7'},
    ]

    poems = [
        {'title': 'poem1',
         'user': 'test',
         'articletitle': 'title1',
         'text': 'text1'},
        {'title': 'poem2',
         'user': 'test1',
         'articletitle': 'title2',
         'text': 'text2'},
        {'title': 'poem3',
         'user': 'test2',
         'articletitle': 'title3',
         'text': 'text3'},
        {'title': 'poem12',
         'user': 'test',
         'articletitle': 'title12',
         'text': 'text12'},
        {'title': 'poem1',
         'user': 'test',
         'articletitle': 'title1',
         'text': 'text1'},
        {'title': 'poem1',
         'user': 'test',
         'articletitle': 'title1',
         'text': 'text1'},

    ]