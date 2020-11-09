from model.model import Model
from preprocessing import doc
from evaluation.statistics import evaluate
from Span import select_spans
from slovnet.markup import SpanMarkup
from evaluation.render import render_box_markup, render_ascii_markup
from slovnet.markup import show_span_box_markup

#file_name = 'data/Новая разметка/Абалкин Л.И._Неиспользованный шанс/Копия Абалкин_Л.И._Неиспользованный шанс_Солдатова_Глафира.docx'
file_name = 'data/Новая разметка/Аджубей_Те 10 лет/Аджубей А._Те десять лет.docx'

d = doc(file_name)

model = Model()

markup = SpanMarkup(d.text, select_spans(model.fit(d.text).spans, 'PER'))

st = evaluate(d.spans, markup.spans)
print(st)

render_box_markup(d, markup)
render_box_markup(d, File_Name='first.html')
render_box_markup(markup, File_Name='second.html')
