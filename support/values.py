# Dictionary and list values used in various text analysis functions 
# Created by David Easton @ d-easton, 28.03.2020

"""
English vowels
"""
vowels = ["a","e", "i", "o", "u"]

"""
English consonants
"""
consonants = ["b","c","d","f","g","h","j","k","l","m","n","p","q"
        "r","s","t","v","x","y","z"
    ]


"""
Stop words are commonly used words deemed unimportant in many NLP circumstances
"""
stop_words = [
    "i", "me", "my", "myself", "we", "our", "ours", "ourselves", 
    "you", "your", "yours", "yourself", "yourselves", "he", "him", "y'all",
    "his", "himself", "she", "her", "hers", "herself", "it", "its", 
    "itself", "they", "them", "their", "theirs", "themselves", "what",
    "which", "who", "whom", "this", "that", "these", "those", "am", "is",
    "are", "was", "were", "be", "been", "being", "have", "has", "had", "now",
    "having", "do", "does", "did", "doing", "a", "an", "the", "and", "don",
    "but", "if", "or", "because", "as", "until", "while", "of", "at", "should", 
    "by", "for", "with", "about", "against", "between", "into", "through", 
    "during", "before", "after", "above", "below", "to", "from", "up", "down", 
    "in", "out", "on", "off", "over", "under", "again", "further", "then", "once", 
    "here", "there", "when", "where", "why", "how", "all", "any", "both", "each",
    "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", 
    "own", "same", "so", "than", "too", "very", "s", "t", "can", "will", "just",
    "ye", "thou", "thine", "anybody", "everybody", "nobody", "therefore",
    ]

stemming_suffixes = [
    "s", "es", "ies", 
]