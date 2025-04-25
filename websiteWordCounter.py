#!/usr/bin/env python3

import requests as r
import re
from bs4 import BeautifulSoup as bs

PAGE_URL = 'http://wikipedia.org'
# basic requests get request syntax w/ error checking for non-200 responses
def grab_page(url):
    resp = r.get(url)

    if resp.status_code != 200:
        print(f'Uh-ohhh! We got {resp.status_code} status code, which is not 200. Aborting mission..')
        exit(1)
    # read the response as byte (.content) then convert bytes to text string (.decode()) - more accurate
    # than the .text method
    return resp.content.decode()

def count_occurences_in(word_list):
    # for word in all_words:
    #    word_count[word] = word_count.setdefault(word, 0) + 1
    # create an empty dictionary to hold words and counts.
    word_count = {}
    # iterate over word_bank. If the word isn't in the dictionary yet, add it with counter 1
    for word in word_list:
        if word not in word_count:
            word_count[word] = 1
    # if word key is already present, increase its value by 1
        else:
            current_count = word_count.get(word)
            word_count[word] = current_count + 1
    return word_count

def get_all_words_from(url):
    # perform the request
    html = grab_page(url)
    # use beautifulsoup and python's html.parser to parse the document into html
    soup = bs(html, 'html.parser')
    # parse text from bs object into new string
    raw_text = soup.get_text()
    # print(raw_text)
    # use re regex library to convert raw_text string into list of words
    # *+, ++, ?+
    # a*a will match 'aaaa' because the a* will match all 4 'a's, but, when the final 'a' 
    # is encountered, the expression is 
    # backtracked so that in the end the a* ends up matching 3 'a's total, and the fourth 'a' 
    # is matched by the final 'a'.
    return re.findall(r'\w+', raw_text)

# sort words by most common
def get_top_words_from(all_words):
    occurrences = count_occurences_in(all_words)
    return sorted(occurrences.items(), key=lambda item: item[1], reverse=True)

all_words = get_all_words_from(PAGE_URL)
top_words = get_top_words_from(all_words)

for i in range(10):
    print(top_words[i][0])