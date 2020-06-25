#!/bin/python3

from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np
import re
import random

# USAGE: This code can be used to scrape a set of known URLS (with a user submitted file as INFILE) or
# can generate a set of random users (through a number provided by the user)
INFILE = input('Path to URL list: ')
INRAND = input('Number of random participants to scrape: ')
CODE = input('Treatment code: ')
OUTFILE = input('Outfile name (ends in .csv): ')
try:
    CODE = int(CODE)
    OUTFILE = True
except:
    print('Error. Please check treatment code or outfile name.')
    quit()

treatments = []
names = []
sinces = []
collections = []
recipes = []
articles = []
followings = []
followers = []
cws = []
cfs = []
tks = []
if INFILE:
    FILE = open(INFILE)
    #FILE = open("../2016_2019.txt")
    LINES = FILE.readlines()
elif INRAND:
    INRAND = int(INRAND)
    LINES = []
    for i in range(INRAND):
        n = random.randint(1,2040455)
        y = 'https://food52.com/users/' + str(n)
        LINES.append(str(y))
    #LINES = rand.readlines()
else:
    print('Input Error. Check input file or random number.')
for LINE in LINES:
    result = requests.get(LINE)
    if result.status_code == 200:
        src = result.content
        soup = BeautifulSoup(src,'lxml')
        treatment = CODE
        treatments.append(treatment)
        #scrape username
        name = soup.find_all('a')[8]
        #nametext = name.text
        names.append(name.text)
        #scrape member since
        since = soup.find('p', class_ ='memeber-since').text
        since = re.sub(r'Member since ', '', since)
        sinces.append(since)
        #scrape number of saved collections
        collection = soup.find('li', class_='current').a.span.text
        if collection:
            collection = str(collection)
        else:
            collection = 0
        collections.append(int(collection))
        #scrape number of contributed recipes
        recipe = soup.select('a[title*="Recipes added by"]')
        if recipe:
            recipe = str(recipe)
            recipe = re.sub(r'\n', '', recipe)
            recipe = re.sub(r'^.*?count">', '', recipe)
            recipe = re.sub(r'\</span>              Recipe', ' ', recipe)
            recipe = recipe.split(' ')[0]
            recipe = re.sub(r'\,', '', recipe)
        else:
            recipe = 0
        recipes.append(int(recipe))
        #scrape number of contributed articles
        article = soup.select('a[title*="Articles by"]')
        if article:
            article = str(article)
            article = re.sub(r'\n', '', article)
            article = re.sub(r'^.*?count">', '', article)
            article = re.sub(r'\</span>              Article', ' ', article)
            article = article.split(' ')[0]
            article = re.sub(r'\,', '', article)
        else:
            article = 0
        articles.append(int(article))
        #scrape number of people following
        following = soup.select('a[href*="following"]')
        if following:
            following = str(following)
            following = re.sub(r'\n', '', following)
            following = re.sub(r'^.*?count">', '', following)
            following = re.sub(r'</span>            Following</a>]', '', following)
            following = re.sub(r'\,', '', following)
        else:
            following = 0
        followings.append(int(following))
        #scrape number of followers
        follower = soup.select('a[href*="followers"]')
        if follower:
            follower = str(follower)
            follower = re.sub(r'\n', '', follower)
            follower = re.sub(r'^.*?count">', '', follower)
            follower = re.sub(r'</span>            Follower', ' ', follower)
            follower = follower.split(' ')[0]
            follower = re.sub(r'\,', '', follower)
        else:
            follower = 0
        followers.append(int(follower))
        #scrape number of contest wins
        cw = soup.select('a[title*="View winning recipes"]')
        if cw:
            cw = str(cw)
            cw = re.sub(r'\n', '', cw)
            cw = re.sub(r'^.*?count">\(', '', cw)
            cw = re.sub(r'\)</span></a>]', '', cw)
            if cw.startswith('['):
                cw = 1
        else:
            cw = 0
        cws.append(int(cw))
        #scrape number of contests as a finalist
        cf = soup.select('a[title*="View finalist recipes"]')
        if cf:
            cf = str(cf)
            cf = re.sub(r'\n', '', cf)
            cf = re.sub(r'^.*?count">\(', '', cf)
            cf = re.sub(r'\)</span></a>]', '', cf)
            if cf.startswith('['):
                cf = 1
        else:
            cf = 0
        cfs.append(cf)
        #scrape number of test kitchen approved recipes
        tk = soup.select('a[title*="View test kitchen"]')
        if tk:
            tk = str(tk)
            tk = re.sub(r'\n', '', tk)
            tk = re.sub(r'^.*?count">\(', '', tk)
            tk = re.sub(r'\)</span></a>]', '', tk)
            if tk.startswith('['):
                tk = 1
            else:
                tk = int(tk)
        else:
            tk = 0
        tks.append(tk)
    else:
        print(LINE)

df = pd.DataFrame({'treatments': treatments,
'users': names,
'member_since': sinces,
'num_collections': collections,
'num_recipes': recipes,
'num_articles': articles,
'following': followings,
'followers': followers,
'contest_wins': cws,
'contest_finalists': cfs,
'test_kitch_approved': tks,
})
print(df.info())
df
df.to_csv(OUTFILE)
