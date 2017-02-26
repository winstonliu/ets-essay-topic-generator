'''! Prompt generator.

'''

import random
import shelve

import scraper

def save_objects(issues, arguments, filename="prompts.shelve"):
    shelved_data = shelve.open(filename, writeback=True)
    shelved_data['issues'] = issues
    shelved_data['arguments'] = arguments
    shelved_data.sync()
    shelved_data.close()

'''! Opens saved shelve files

    @returns Tuple of form (issues, arguments) where both are Prompt objects

'''
def open_savefile(filename="prompts.shelve"):
    shelved_data = shelve.open(filename)
    issues = shelved_data['issues']
    arguments = shelved_data['arguments']
    shelved_data.close()

    return (issues, arguments)

class PromptGenerator:
    '''! Scrape topics from the passed in website. '''
    def __init__(self, website):
        self._prompts = scraper.scrape_and_parse(website)
        self._shown_prompts = list()

    def __len__(self):
        return len(self._prompts)

    '''! Randomly picks a prompt from the list of unshown prompts.

        @returns Prompt object

    '''
    def generate_prompt(self):
        selected_idx = random.randint(0, len(self))
        # Prevents any shallow copy issues
        prompt = self._prompts[selected_idx].copy()
        self._shown_prompts.append(prompt)
        del self._prompts[selected_idx]
        return prompt

    '''! Clear the shown topics lists. '''
    def reset(self):
        self._prompts.extend(self._shown_prompts)
        self._shown_prompts = list()
