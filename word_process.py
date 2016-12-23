import numpy as np
import pandas as pd
import seaborn as sb
import re
from nltk.corpus import stopwords
from nltk import FreqDist

def clear_stopwords(context):
    letters = re.sub("[^a-zA-Z]", " ", context)
    context = letters.lower().split()
    stopword = set(stopwords.words('english'))
    clear = [c for c in context if c not in stopword]
    return clear

def clear_html(raw_html):
  cleanr = re.compile('<.*?>')
  cleantext = re.sub(cleanr, '', raw_html)
  return cleantext

def get_word_list(data):
    content_word_list = []
    title_word_list = []
    tag_word_list = []
    print len(data['content'])
    for content in data['content']:
        content_word_list += clear_stopwords(clear_html(content))
    for title in data['title']:
        title_word_list += clear_stopwords(title)
    for tag in biology['tags']:
        tag_word_list += tag.split()
    fdist_title = FreqDist(title_word_list)
    fdist_content = FreqDist(content_word_list)
    fdist_tags = FreqDist(tag_word_list)
    return {"fdist_title": fdist_title, "fdist_tags": fdist_tags, "fdist_content": fdist_content}

biology = pd.read_csv("./input/diy.csv")
fdist = get_word_list(biology)

fdist['fdist_tags'].plot(50,cumulative=True)
