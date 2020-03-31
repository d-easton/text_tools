# functions for text analysis

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
    Remove duplicates from a list of tokens by converting into dictionary and back
        tokens -- list of tokens to clean
    """
    return list(dict.fromkeys(tokens))

def word_count(tokens):
    """
    Generate word count dictionary from list of tokens
    """
    wc = {}
    for t in tokens:
        wc[t] = wc[t]+1 if t in wc else 1 
    return wc

