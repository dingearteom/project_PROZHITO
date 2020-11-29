from navec import Navec
from slovnet import NER
from pullenti_wrapper.processor import DATE, Processor
from slovnet.span import Span
import sys

class Model:
    def __init__(self):
        print(sys.path)
        self.navec = Navec.load('data/navec_news_v1_1B_250K_300d_100q.tar')
        self.ner = NER.load('data/slovnet_ner_news_v1.tar')
        self.ner.navec(self.navec)

    def fit(self, document):
        return self.ner(document).spans

class Date:
    def __init__(self, date, span):
        self.span = span
        self.day = None
        self.month = None
        self.year = None
        m = {'DAY': 'day', 'MONTH': 'month', 'YEAR': 'year'}

        def get_date(object, date_):
            for slot in date_.slots:
                if (slot.key in ['DAY', 'MONTH', 'YEAR']):
                    Date.__setattr__(object, m[slot.key], int(slot.value))
                elif (slot.key == 'HIGHER'):
                    get_date(object, slot.value)
                else:
                    raise NameError("Unknown key.")
                    # if (not slot.key in ['POINTER', 'ISRELATIVE', 'QUARTAL']):
                    #     print(slot.key)
                    #     raise NameError("Unknown key.")
            return
        get_date(self, date)
    def __str__(self):
        return (("Day:" + str(self.day)) if (not self.day is None) else "") \
               + (" Month:" + str(self.month) if (not self.month is None) else "") \
               + (" Year:" + str(self.year) if (not self.year is None) else "")

class DateRange:
    def __init__(self, date, span):
        try:
            self.span = span
            self.start = None
            self.stop = None
            for slot in date.slots:
                if (slot.key == 'FROM'):
                    self.start = Date(slot.value, Span(0, 0))
                elif (slot.key == 'TO'):
                    self.stop = Date(slot.value, Span(0, 0))
                else:
                    raise NameError('Unknown label while parsing DateRange')
        except Exception as exc:
            print(date)
            raise(exc)

    def __str__(self):
        return "From " + self.start.__str__() + " To " + self.stop.__str__() + "\n"


def fit_time(document):
    processor = Processor([DATE])
    print("Initialisation done.")
    result = processor(document)
    dates = []

    for match in result.matches:
        if (match.referent.label == 'DATE'):
            try:
                dates.append(Date(match.referent, match.span))
            except:
                pass
        elif (match.referent.label == 'DATERANGE'):
            try:
                dates.append(DateRange(match.referent, match.span))
            except Exception as exc:
                print(document[match.span.start: match.span.stop])
                raise exc
        else:
            raise NameError('Unknown time entity type.')
    return dates


def delete_red_per(spans, d):
    # is not implemented yet
    pass
