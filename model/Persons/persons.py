class Persons_extractor:
    def __init__(self):
        pass
    def fit(self, document, spans):
        persons = []
        id = 1
        for span in spans:
            persons.append(Person(span, id))
            id += 1
        return persons

class Person:
    def __init__(self, span, id):
        self.span = span
        self.id = id

