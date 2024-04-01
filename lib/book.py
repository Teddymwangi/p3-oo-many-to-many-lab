

class Book:
    members = []

    def __init__(self, title):
        self.title = title
        self.members.append(self)
