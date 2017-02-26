#!/usr/bin/env python

import os
import sys

# Append prompt_generator path. Alternative is to write a setup.py and install prompt_generator
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir, 'src'))

import prompt_generator


DEFAULT_SAVEPATH = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), os.pardir, 'savefiles', 'prompts.shelve')

if __name__=="__main__":
    try:
        issues, arguments = prompt_generator.open_savefile(DEFAULT_SAVEPATH)
    except:
        print "Could not open savefile, reloading from website."
        # Get pool of issues and arguments
        issues = prompt_generator.PromptGenerator(
                "https://www.ets.org/gre/revised_general/prepare/analytical_writing/issue/pool")
        arguments = prompt_generator.PromptGenerator(
                "https://www.ets.org/gre/revised_general/prepare/analytical_writing/argument/pool")

    # Pick a random issue
    issue_prompt = issues.generate_prompt()

    print "\n##########\nISSUE TOPIC:\n"
    print issue_prompt.topic +'\n' 
    print issue_prompt.instructions

    # Pick a random argument
    argument_prompt = arguments.generate_prompt()

    print "\n##########\nARGUMENT TOPIC:\n"
    print argument_prompt.topic + '\n'
    print argument_prompt.instructions

    prompt_generator.save_objects(issues, arguments, DEFAULT_SAVEPATH)

    print "\nPress Enter to continue..."
    raw_input()
