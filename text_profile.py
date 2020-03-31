class TextProfile:
    """
    Basic class for grouping statistic and descriptive info about a particular text
    """

    def __init__(self, title, author, length):
        self.title = title
        self.author = author
        self.length = length

    #TODO: Compare method