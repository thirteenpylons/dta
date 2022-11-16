"""
from data.manipulation import String
"""


class Email:
    """
    Create methods that will identify patterns of the email to extract the
    correct name if the name exists.
    """
    def __init__(self, recipient: str):
        self.recipient = recipient

    def extract_first_name(self) -> str:
        if self.recipient.startswith("C-"):
            delimiter = self.recipient.find(".")
            name = self.recipient[2:3].upper() + self.recipient[3:delimiter]
        else:
            delimiter = self.recipient.find(".")
            name = self.recipient[:1].upper() + self.recipient[1:delimiter]
        return name


class Extract:
    """
    Class is built to assist with data extraction.

    """
    def __init__(self, data: str):
        self.data = data

    def count_occurence(self, target: str) -> int:
        """
        Used to count the occurence of the given target.
        If I wanted to know how many times the name "David" shows up in
            a given data set I would use this.
        
        use:
            count_occurence("David")
        
        Parameter target:
        Precondition:
        """
        pass