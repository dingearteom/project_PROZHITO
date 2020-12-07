from model.Dates.dates import Dates
from slovnet.span import Span
from model.Paragraphs.DOC import DOC

class Diary_Par:
    def __init__(self):
        pass
    def fit(self, document):
        model_time = Dates()
        dates = model_time.fit(document)
        d = DOC(document)
        paragraphs = []
        start = 0

        def strip(start, end):
            while (d.text[start] in ['\n', ' '] and start + 1 < end):
                start += 1
            while (d.text[end - 1] in ['\n', ' '] and start + 1 < end):
                end -= 1
            return (start, end)

        for date in dates:
            if (date.to_num() == 3 or date.to_num() == 7):
                span = d.paros[d.paros_id(date.span)]

                if (span.start > start):
                    beg = start
                    end = span.start
                    beg, end = strip(beg, end)
                    paragraphs.append(Span(beg, end, type='Paragraph'))
                    start = span.start
        beg = start
        end = len(d.text)
        beg, end = strip(beg, end)
        paragraphs.append(Span(beg, end, type='Paragraph'))
        return paragraphs