#!/bin/python3
import os
from typing import Dict, Tuple
import frontmatter
import csv

#def parse_YAML(f:str) -> Dict[str, TODO]:
def parse_YAML(file:str, verbose=False):
    with open(file, 'r', encoding='utf-8') as f:
        try:
            if verbose: print(f"Parsing {file}")
            metadata, content = frontmatter.parse(f.read())
            return metadata, content
        except:
            print("An error occurred while parsing YAML from markdown file")


def parse_tools(tools_dir):
    tools = []
    for root, dirs, files in os.walk(tools_dir):
        for f in files:
            if f.endswith('.md') and not 'index' in f:
                tools.append(parse_YAML(os.path.join(root, f), verbose=True))
    return tools

def info(tool:Tuple):
    metadata, content = tool
    print(metadata.keys())
    print(content)

def get_all_fields(tools:list):
    '''
    Method to get the complete list of metadata fields used in all posts
    Just to add some robustness against missing fields in some entries
    '''
    fields = set()
    for metadata, content in tools:
        for key in metadata.keys():
            if key not in fields:
                fields.add(key)
    return sorted(fields)
        
def to_csv(tools, verbose=False):
    fields = ['title', 'values', 'repo', 'description', 'categories', 'phases', 'languages', 'licence', 'references' ]
    fields_check = get_all_fields(tools)
    fields_check.append('description')

    if len(set(fields_check).difference(set(fields)))!=0:
        print("WARNING: fields variable does not include all fields")
        print("Compare:")
        print("Fields: ", fields)
        print("Fields ref.: ", fields_check)

    print(fields)
    with open('tools.csv', 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fields, dialect='excel')
        writer.writeheader()

        for metadata, content in tools:
            data = metadata 
            data['description'] = content.replace("\n", " ")
            writer.writerow(data)


if __name__ == '__main__':
    file_dir = os.path.dirname(__file__)
    tools_dir = os.path.join(file_dir, '../../content/tools/')
    tools = parse_tools(tools_dir)
    to_csv(tools, verbose=True)
