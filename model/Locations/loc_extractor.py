

class LOC_extractor:
    def __init__(self):
        pass
    def fit(self, document, spans):
        loc = []
        for span in spans:
            loc.append(LOC(span, document[span.start:span.stop]))
        return loc


class LOC:
    def __init__(self, span, text):
        self.span = span
        self.text = text
