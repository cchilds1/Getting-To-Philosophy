#!/usr/bin/python
import re
import requests
import sys

from bs4 import BeautifulSoup


PHILOSOPHY_URL = 'https://en.wikipedia.org/wiki/Philosophy'
MAX_HOPS = 100

def remove_paren(p_text):
    '''
    remove_paren takes in the page text
    and removes all text between parentheses
    and brackets before returning the text.
    '''
    text, num_replaced = re.subn(r'\([^()]*\)(?!\")|\[[^\[\]]*\](?!\")', '', p_text)
    while num_replaced:
        # here we only remove pairs of parentheses without other parentheses 
        # in the middle so we can deal with nesting appropriately
        text, num_replaced = re.subn(r'\([^()]*\)(?!\")|\[[^\[\]]*\](?!\")', '', text)
    return text

def get_next_url(url):
    '''
    get_next_url takes in the url string and returns
    the first url found in the main paragraph of the 
    page that is not within parentheses, brackets, or italicized.
    If the next url is not found, we return an error string.
    '''
    try:
        reqs = requests.get(url)
    except requests.exceptions.RequestException as e:
        return None, str(e)

    # remove the text between parentheses and brackets
    s = remove_paren(reqs.text)
    soup = BeautifulSoup(s, 'html.parser')

    # remove italics from the page - we only want urls that are in bold or plain text
    italics = soup.find_all('i')
    if italics:
        for italic in italics:
            italic.extract()

    paragraphs = soup.find(id='mw-content-text').find(class_='mw-parser-output').find_all('p', recursive=False)

    for p in paragraphs:
        urls = p.find_all('a', href=True)
        for url in urls:
            if url and url['href'].startswith('/wiki'):
                return 'https://en.wikipedia.org' + url.get('href'), None
    
    return None, 'unable to find next url'
                
def find_philosophy(url):
    '''
    find_philosophy takes in the starting url string 
    and returns the number of hops it takes to hit the
    philosophy page or reach the MAX_HOPS limit.
    '''
    hops = 0
    print(url)
    while hops < MAX_HOPS:
        result = get_next_url(url)
        url = result[0]
        err_string = result[1]
        hops+=1

        # return an error if we could not find the next url
        if not url and err_string:
            raise Exception(err_string)

        print(url)

        # return the number of hops if we find the philosophy url
        if url == PHILOSOPHY_URL:
            return hops

    return hops
        
if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('need to include starting URL as an argument')
    else:
        starting_url = sys.argv[1]
        try: 
            hops = find_philosophy(starting_url)
            print('hops ' + str(hops))
        except Exception as e:
            print(str(e))
