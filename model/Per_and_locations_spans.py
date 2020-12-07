from navec import Navec
from slovnet import NER
from Span import select_spans

class Per_and_Loc:
    def __init__(self):
        navec = Navec.load('data/navec_news_v1_1B_250K_300d_100q.tar')
        self.ner = NER.load('data/slovnet_ner_news_v1.tar')
        self.ner.navec(navec)
    def fit(self, document):
        return {'PER': select_spans(self.ner(document).spans, ['PER']),
                'LOC': select_spans(self.ner(document).spans, ['LOC'])}
