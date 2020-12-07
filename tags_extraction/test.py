import os
import sys

##
os.chdir('..')
del(sys.path[0])
sys.path.insert(0, os.getcwd())
##



from tags_extraction.DOC import DOC
from evaluation.render import render_box_markup
from slovnet.markup import SpanMarkup
from ipymarkup.palette import palette, PURPLE, RED, GREEN
from model.Dates.dates import Dates

file_name = "data/Новая разметка/Сахновская Наталья/Сахновская_Наталья_23.VI.1941-22.VII.1944_Горбатенко_Яна.docx"
d = DOC(file_name, tags_deletion=False)
# model_time = Dates()
# dates_spans = model_time.fit(d.text)
#
# for date in dates_spans:
#     paros_id = d.paros_id(date.span)
#     print(paros_id)
#     print(date.span)
#     print(d.text[date.span.start:date.span.stop])
#     print(d.text[d.paros[paros_id].start: d.paros[paros_id].stop])
#     print('****')
render_box_markup(SpanMarkup(d.text, d.paragraphs), File_Name='tags_extraction/data/paragraphs.html')
#render_box_markup(SpanMarkup(d.text, d.per), File_Name='per.html')

