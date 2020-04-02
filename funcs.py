# Support functions for basic text analysis 
# Created by David Easton @ d-easton, 28.03.2020

from .support.values import stop_words

def tokenize(raw, lower=True):
    """
    Tokenize breaks a string of raw text into a list of string tokens
        raw -- input string
        lower -- Flag to cast variables to lowercase
    """
    punctuation = ".!?;:"
    raw = raw.lower().split() if lower else raw.split()
    tokens = [token.strip(punctuation)
        .replace('.', '')
        .replace(',', '')                
        .replace('!', '') 
        .replace('?', '')
        .replace(';', '')
        .replace(':', '')        
        for token in raw]
    return tokens 

def remove_duplicates(tokens):
    """
    Remove duplicates from a list of tokens by converting into dictionary, returns list converted back from dictionary
    """
    return list(dict.fromkeys(tokens))

def word_count(tokens):
    """
    Returns dictionary of word counts from list of tokens
    """
    wc = {}
    for t in tokens:
        wc[t] = wc[t]+1 if t in wc else 1 
    return wc

def calc_ttr(tokens):
    """
    Return the type-token ratio (TTR), or the ratio of unique entries over total entries, given a list of tokens
    """
    return (float(len(word_count(tokens)))) / len(tokens)

# TODO: syntactic complexity -- how to determine if things are noun or verb?

def remove_stop_words(tokens):
    """
    Remove common stop words from list of tokens (see full list in .support.values)
    """
    output = []
    for t in tokens:
        if t not in stop_words:
            output.append[t]
    return output


# Stemming via stripping
def stem_strip_suffix(token):
    """
    Perform basic stemming by stripping a suffix off a token
    """
    # Note: flawed implmentation right now

