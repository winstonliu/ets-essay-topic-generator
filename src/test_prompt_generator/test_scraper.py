#!/usr/bin/env python

import os, sys

# Append prompt_generator path. Alternative is to write a setup.py and install prompt_generator
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir))

import prompt_generator

# TODO Make this a legit unit test
if __name__=="__main__":

    list_of_issues = prompt_generator.scrape_and_parse("https://www.ets.org/gre/revised_general/prepare/analytical_writing/issue/pool")
    list_of_arguments = prompt_generator.scrape_and_parse("https://www.ets.org/gre/revised_general/prepare/analytical_writing/argument/pool")

    with open('arguments.txt', 'w') as f:
        for a in list_of_arguments:
            f.write(a.topic)
            f.write(a.instructions)

    with open('issues.txt', 'w') as f:
        for a in list_of_issues:
            f.write(a.topic)
            f.write(a.instructions)

