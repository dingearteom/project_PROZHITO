from navec import Navec
from slovnet import NER
from slovnet.span import Span
from Span import select_spans
from slovnet.markup import SpanMarkup

class Model:
    def __init__(self):
        self.navec = Navec.load('data/navec_news_v1_1B_250K_300d_100q.tar')
        self.ner = NER.load('data/slovnet_ner_news_v1.tar')
        self.ner.navec(self.navec)

    def fit(self, document):
        return self.ner(document)
