import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
import re
from urllib.request import urlopen

from tqdm import tqdm

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


def getLevelNames(text):
    # Get the paragraph under the strong tag labeled "Entrances"
    _out = soup.find(['strong', 'span'], text=text).find_next('p')

    # Find all Level links in the paragraph filtering all the other links
    _out = _out.find_all('a', href=re.compile('level-'))
    output = []
    for n in _out:
        output.append(n.text)
        
    # Remove duplicates
    output = list(dict.fromkeys(output))

    # Remove any strings that do not fit the regex pattern of "Level [number]"
    output = [x for x in output if re.match(r'Level \d+', x)]
    return output


normal_levels_enter_exit = []
for href in tqdm(normal_levels_href[0:5]):
    try:
        url = "http://backrooms-wiki.wikidot.com" + href
        page = urlopen(url)
        soup = BeautifulSoup(page, 'html.parser')
    except:
        continue

    try:
        entrances = getLevelNames('Entrances:')
    except:
        try:
            entrances = getLevelNames('Entrances')
        except:
            entrances = []
    
    try:
        exits = getLevelNames('Exits:')
    except:
        try:
            exits = getLevelNames('Exits')
        except:
            exits = []

    normal_levels_enter_exit.append({"Level" : href, "Entrances" : entrances, "Exits" : exits})


# Print normal_levels_enter_exit in a nice format
for level in normal_levels_enter_exit:
    print(level['Level'])
    print('Entrances:')
    for entrance in level['Entrances']:
        print(entrance)
    print('Exits:')
    for exit in level['Exits']:
        print(exit)
    print()






