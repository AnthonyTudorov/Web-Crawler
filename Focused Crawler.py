from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import ssl
import os

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

def get_page_content(url):
    try:
        html_response_text = urlopen(url).read()
        page_content = html_response_text.decode( 'utf-8' )
        return page_content
    except Exception as e:
        return None

# soup = BeautifulSoup(page_content, 'html.parser')
# page_text = soup.get_text()

def clean_title(title):
    invalid_characters = ['<', '>', ':', '"', '/', '\\', '|', '?', '*']
    for c in invalid_characters:
        title.replace(c,'')
    return title

# if re.search(term, page_text, re.I) :

def get_urls(soup):
    links = soup.find_all('a')
    urls=[]
    for link in links:
        urls.append(link.get('href'))
    return urls

def is_url_valid(url):
    if url is None:
        return False
    if re.search('#', url):
        return False
    match=re.search('^/wiki/', url)
    if match:
        return True
    else:
        return False

def reformat_url(url):
    match=re.search('^/wiki/', url)
    if match:
        return "https://en.wikipedia.org"+url
    else:
        return url

def save(text, path):
    f = open(path, 'w', encoding = 'utf-8', errors = 'ignore')
    f.write(text)
    f.close()

# f = open("crawled_urls.txt", "w")
# i = 1
# for url in crawled_urls:
#     f.write(str(i) + ': ' + url + '\n')
#     i += 1
# f.close()

def focused_crawler(seed_urls: list, related_terms: list):
    queue = seed_urls
    visited_urls = set(seed_urls)
    page_count = 0
    saved_urls = []
    while queue:
        url = queue.pop()
        page_content = get_page_content(url)
        if page_content is None:
            continue
        term_count = 0
        soup = BeautifulSoup(page_content, 'html.parser')
        page_text = soup.get_text()
        for term in related_terms:
            if re.search(term, page_text, re.I):
                term_count += 1
                if term_count >= 2:
                    page_title = clean_title(soup.title.string)
                    save(page_title + ", " + page_content, "results")
                    saved_urls.append(url)
                    visited_urls.add(url)
                    page_count += 1
                    break
        if page_count >= 500:
            break
        outgoing_urls = get_urls(soup)
        for outgoing_url in outgoing_urls:
            if 


focused_crawler(["https://en.wikipedia.org/wiki/World_War_II"], [])