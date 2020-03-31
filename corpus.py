
from .text_profile import TextProfile
from .support.errors import CorpusConstructionError

class Corpus:
    """
    Corpus class for grouping together several text profiles
    atrs:
        - works -- {title, text_profile} of all works associated with this Corpus
        - composite -- flag for if Corpus allows works from multiple authors
        - author -- required specification of author if non-composite Corpus, else None
        - allow_duplicates -- does this Corpus allow identical text_profiles, even if identified
                                by different titles?

    """

    def __init__(self, composite=True, author=None, allow_duplicates=False):
        """
        Create a new Corpus object
            composite -- does this Corpus allow works from multiple authors?
            author -- required specification of author surname if non-composite Corpus
            allow_duplicates -- are duplicate TextProfiles allwoed in this Corpus?
        """
        if not composite and not author:
            raise CorpusConstructionError('Non-composite Corpus must have author specified upon construction.')
        else:
            self.composite = composite
            self.author = author
            self.profiles = {}

    def add_text(self, text):
        """
        Adds new TextProfile to Corpus, identified by title of new TextProfile
            text -- TextProfile item to be added to the Corpus
        """
        title = text.title
        if title in self.profiles:
            print(f"Failed to add {text.author}\'s text '{title}' -- text already in corpus")
            return 0
        else:
            self.profiles[title] = text

        #TODO: Compare TextProfile values when allow_duplicates is false

    def get_title_author_strings(self):
        """
        Return a list of strings describing all works in the Corpus by title and author
            e.g. 'Hamlet by Shakespeare'
        """
        output = []
        for text in list(self.profiles.values()):
            output.append(f"{text.title} by {text.author}")
        return output

    def get_avg_text_length(self, round_whole=False):
        """
        Return average length of text for this Corpus
            - round_whole -- optional ability to round returned float to nearest whole number
        """
        sum = 0.0
        profile_list = list(self.profiles.values())
        for text in profile_list:
            sum += text.length
        return round(sum/len(profile_list)) if round_whole else sum/len(profile_list)
        