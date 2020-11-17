from tags_extraction.DOC import DOC
from evaluation.render import render_box_markup

#file_name = 'data/Новая разметка/Абалкин Л.И._Неиспользованный шанс/Копия Абалкин_Л.И._Неиспользованный шанс_Солдатова_Глафира.docx'
file_name = 'data/Новая разметка/Аджубей_Те 10 лет/Аджубей А._Те десять лет.docx'

d = DOC(file_name=file_name)

render_box_markup()
# model = Model()
#
# markup_with_LOC = SpanMarkup(d.text, select_spans(model.fit(d.text).spans, ['PER', 'LOC']))
# markup = SpanMarkup(d.text, select_spans(markup_with_LOC.spans, ['PER']))

# st = evaluate(d.spans, markup.spans)
# print(st)

# render_box_markup(d, markup)
# render_box_markup(d, File_Name='first.html')
# render_box_markup(markup, File_Name='second.html')
# render_box_markup(markup_with_LOC, File_Name='second_with_LOC.html')
