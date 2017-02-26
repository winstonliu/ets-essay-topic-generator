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
        topic_string = str()
        iter_tag = topic_header.find_next_sibling()
        while iter_tag.name != 'div':
            # Check if string is valid
            if iter_tag.string == None: 
                break

            topic_string += iter_tag.string
            # Increment to next tag
            iter_tag = iter_tag.find_next_sibling()
        
        # Instructions are one level down, in an indented class
        # These are one paragraph only. 
        # If ETS changes it to multiple paragraphs, then we have problem
        instruction_string = iter_tag.contents[1].string 

        prompt_obj = Prompt(topic_string, instruction_string)
        prompt_list.append(prompt_obj)

    return prompt_list 

class Prompt:
    '''! Class for storing topics and instructions

    '''
    def __init__(self, topic, instructions):
        self.topic = topic.encode('ascii', 'replace')
        self.instructions = instructions.encode('ascii', 'replace')

    def copy(self):
        return copy.deepcopy(self)

