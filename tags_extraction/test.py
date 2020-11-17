from DOC import DOC
from evaluation.render import render_box_markup
from slovnet.markup import SpanMarkup

file_name = '../data/Новая разметка/Непорожний П.С .Энергетика страны глазами министра _ Дневники/Артёмова РГГУ ФК 2 курс практика Непорожний П.С. 1959-1966.docx'
d = DOC(file_name, tags_deletion=False)

render_box_markup(SpanMarkup(d.text, d.paragraphs), File_Name='paragraphs.html')
#render_box_markup(SpanMarkup(d.text, d.per), File_Name='per.html')

