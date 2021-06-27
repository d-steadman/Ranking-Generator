"""
An event object that holds an ordered group of swimmers for easy storage and
comparison against event objects from a competing team's events.
"""

class Event:
    def __init__(self, title):
        self.title = title
        self.swimmers = []

    def __str__(self):
        output = ""

        for swimmer in self.swimmers:
            output += str(swimmer) + "\n"

        return output
