import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
import re
from urllib.request import urlopen

normal_levels_url = "http://backrooms-wiki.wikidot.com/normal-levels-i"
normal_levels_page = urlopen(normal_levels_url)


normal_levels_soup = BeautifulSoup(normal_levels_page, 'html.parser')

# Find all the li tags in the soup

normal_levels_li = normal_levels_soup.find_all('li')

# Create a list of all the li tags

normal_levels_list = []

for li in normal_levels_li:
    normal_levels_list.append(li)

# Create a list of all the li tags that contain the level name

normal_levels_list = normal_levels_list[1:]


# Get all of the hrefs attributes from the li tags
normal_levels_href = []

for li in normal_levels_list:
    normal_levels_href.append(li.find('a')['href'])

normal_levels_href = [x for x in normal_levels_href if 'level' in x]
normal_levels_href = normal_levels_href[7:]


# Get the level names without the anchor tags in normal_levels_list
normal_levels_names = []

for li in normal_levels_list:
    normal_levels_names.append(li.text)

normal_levels_names = [x for x in normal_levels_names if 'Level' in x]
normal_levels_names = normal_levels_names[7:]
normal_levels_names = [x.replace('(This article is under rewrite)', '') for x in normal_levels_names]

normal_levels_href = ['/level-18']
normal_levels_enter_exit = []
for href in normal_levels_href:
    url = "http://backrooms-wiki.wikidot.com" + href
    page = urlopen(url)
    soup = BeautifulSoup(page, 'html.parser')

    try:
        # Get the paragraph under the strong tag labeled "Entrances"
        enterances = soup.find('strong', text='Entrances:').find_next('p').text
        enterances = re.findall(r'Level \d+', enterances)

        # Get the paragraph under the strong tag labeled "Exits"
        exits = soup.find('strong', text='Exits:').find_next('p').text
        exits = re.findall(r'Level \d+', exits)
    except:
        enterances = []
        exits = []

    normal_levels_enter_exit.append({"Level" : href, "Enterances" : enterances, "Exits" : exits})






