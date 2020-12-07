from tags_extraction.DOC import DOC as DOC_Extracted
from model.Dates.dates import Dates
from json import JSONEncoder
import copy

# DOC_with_Time
class DOC:
    def __init__(self, file_name):
        d = DOC_Extracted(file_name=file_name)
        self.text = d.text
        self.Paragraphs = []
        paragraphs_spans = d.paragraphs

        model_time = Dates()
        dates_spans = model_time.fit(d.text)

        i = 0
        prev_paros_id = -1

        for par_span in paragraphs_spans:
            dates = []
            while (i < len(dates_spans) and dates_spans[i].span.stop <= par_span.stop):
                paros_id = d.paros_id(dates_spans[i].span)
                first_in_paros = (paros_id != prev_paros_id)
                prev_paros_id = paros_id

                dates.append(Wrap_Date(dates_spans[i], first_in_paros=first_in_paros))
                i += 1

            self.Paragraphs.append(Paragraph(par_span, dates))

    def encode(self):
        d = copy.deepcopy(self.__dict__)
        res = copy.deepcopy(self.__dict__)
        del res['text']
        res['Paragraphs'] = []
        for Paragraph in d['Paragraphs']:
            res['Paragraphs'].append(Paragraph.encode())
        return res

class Paragraph:
    def __init__(self, span, dates):
        self.span = span
        self.dates = dates

    def encode(self):
        d = copy.deepcopy(self.__dict__)
        res = copy.deepcopy(self.__dict__)
        res['span'] = res['span'].__dict__
        res['dates'] = []
        for date in d['dates']:
            res['dates'].append(date.encode())
        return res

class Wrap_Date:
    def __init__(self, date, first_in_paros):
        self.Date = date
        self.first_in_paros = first_in_paros
    def encode(self):
        res = copy.deepcopy(self.__dict__)
        res['Date'] = res['Date'].encode()
        return res

class DOC_Encoder(JSONEncoder):
    def default(self, other):
        return other.encode()