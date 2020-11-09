from navec import Navec
from slovnet import NER
from slovnet.span import Span
import docx
import re
from slovnet.markup import SpanMarkup

def doc(file_name):
    doc_ = "" #text of the document
    spans = []

    file = docx.Document(file_name)

    reg_exp = r"(<персона.*?>)(.*?)(</персона>)"

    y = False
    for para in file.paragraphs:
        para = para.text
        m = re.finditer(reg_exp, para)
        start = []
        end = []
        middle = []
        for s in m:
            y = True
            start.append(s.span(1))
            middle.append(s.span(2))
            end.append(s.span(3))

        ind = 0
        i = 0
        cur_par = ""  # current paragraph

        while (i < len(para)):
            if (ind < len(start) and i == start[ind][0]):
                spans.append(
                    Span(len(doc_) + len(cur_par), len(doc_) + len(cur_par) + (middle[ind][1] - middle[ind][0]),
                         type='PER'))

                i = middle[ind][0]
                while (i < middle[ind][1]):
                    cur_par += para[i]
                    i += 1
                i = end[ind][1]
                ind += 1
            else:
                cur_par += para[i]
                i += 1

        doc_ += cur_par
        doc_ += '\n'
    return SpanMarkup(doc_, spans)