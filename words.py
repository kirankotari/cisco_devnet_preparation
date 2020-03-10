"""Retrieve and print words from a URL.

Useage: 

    python words.py <URL>
"""
import sys
from urllib.request import urlopen


def fetch_words(url):
    """Fetch a list of words from URL.

    Args:
        url: The URL of utf-8 document

    Returns:
        A list of string contains the words from 
        the document.
    """
    story = urlopen(url)
    story_words = []
    for line in story:
        line_words = line.decode('utf-8').split()
        for each in line_words:
            story_words.append(each)
    story.close()
    return story_words


def print_items(items):
    """Print items one per line.

    Args:
        items: An iterable series of printable item.
    """
    for item in items:
        print(item)


def main(url='http://sixty-north.com/c/t.txt'):
    """Print each word from text document from at a URL.

    Args:
        url: The URL of utf-8 document
    """
    words = fetch_words(url)
    print_items(words)


if __name__ == "__main__":
    main(sys.argv[1]) # The 0th arg is the module filename