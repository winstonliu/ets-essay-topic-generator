'''! Does scraping and parsing of topics

'''

import urllib2
from bs4 import BeautifulSoup
import copy

'''! Scrape website and parse according to current ETS format
    
    Will require modification if ETS website format changes.

    @param website Website URL string

    @returns List of Prompt objects

'''
def scrape_and_parse(website):
    # TODO exception handling
    page = urllib2.urlopen(website).read()
    content = BeautifulSoup(page, "lxml")

    prompt_list = list()

    # Website currently uses "divider-50" classes to separate topics
    for topic_header in content.find_all("div", {"class": "divider-50"}):
        # Topic is contained in the next series of <p>/<p> tags
        iter_tag = topic_header.find_next_sibling()
        topic_string, iter_tag = grab_non_div_tag_content(iter_tag)
        # Skip over div string
        iter_tag = iter_tag.find_next()
        # Grab instruction string
        instruction_string, iter_tag = grab_non_div_tag_content(iter_tag)

        prompt_obj = Prompt(topic_string, instruction_string)
        prompt_list.append(prompt_obj)

    return prompt_list 

def grab_non_div_tag_content(tag):
    string = str()
    while tag.name != 'div':
        if not tag.string == None:
            string += tag.string + '\n'
        # Edge case where italics mess us the .string function
        elif tag.name == 'p':
            string += tag.contents[0]

        tag = tag.find_next()

    return (string, tag)

class Prompt:
    '''! Class for storing topics and instructions

    '''
    def __init__(self, topic, instructions):
        self.topic = topic.encode('ascii', 'replace')
        self.instructions = instructions.encode('ascii', 'replace')

    def copy(self):
        return copy.deepcopy(self)

