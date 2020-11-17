from tags_extraction.DOC import DOC
from evaluation.statistics import evaluate, statistics
from evaluation.render import render_box_markup
from slovnet.markup import SpanMarkup
from Span import select_spans
from model import Model
from guppy import hpy
import json
import time
import os

model = Model()
res = statistics()

num_of_doc = 0

with open('data/main_file.txt') as file:
    main_file = json.load(file)
    for key, value in main_file.items():
        for file_name in value:
            num_of_doc += 1
print(num_of_doc)


with open('data/main_file.txt') as file:
    main_file = json.load(file)
    ind = 0
    sum_duration = 0

    for key, value in main_file.items():
        for file_name in value:
            print(file_name)

            start_time = time.time()

            d = DOC(file_name=file_name)
            spans_model = model.fit(d.text).spans
            markup_per = SpanMarkup(d.text, select_spans(spans_model, ['PER']))

            if (not os.path.exists(f"data/render_results/{key}/compare.html")):
                os.system(f"touch data/render_results/\"{key}\"/compare.html")

            render_box_markup(SpanMarkup(d.text, d.per), markup_per, File_Name=f"data/render_results/{key}/compare.html")

            st = evaluate(d.per, markup_per.spans)

            with open(f"data/render_results/{key}/statistics.txt", 'w') as file:
                file.write(st.__str__())

            duration = (time.time() - start_time)
            sum_duration += duration

            print(st)
            ind += 1
            print((ind / num_of_doc) * 100, "%")
            print("Estimated time left: ", ((sum_duration / ind) * (num_of_doc - ind)) / 60, 'min')
            print("Avg_duration: ", sum_duration / ind, 's')
            print("Duration: ", duration, 's')

            res = res + st
print(res)

with open("data/statistics.txt", 'w') as file:
    file.write(res.__str__())



# file_name_second = '../data/Новая разметка/Абалкин Л.И._Неиспользованный шанс/Копия Абалкин_Л.И._Неиспользованный шанс_Солдатова_Глафира.docx'
# file_name = '../data/Новая разметка/Аджубей_Те 10 лет/Аджубей А._Те десять лет.docx'
#
# d = DOC(file_name=file_name)
#
# model = Model()
#
#
#
# spans_model = model.fit(d.text).spans
#
# spans_model_second = model.fit(d_second.text).spans

# markup_with_LOC = SpanMarkup(d.text, select_spans(spans_model, ['PER', 'LOC']))
# markup_per = SpanMarkup(d.text, select_spans(spans_model, ['PER']))

#render_box_markup(SpanMarkup(d.text, d.per), markup_per)
# render_box_markup(d, File_Name='first.html')
# render_box_markup(markup, File_Name='second.html')
# render_box_markup(markup_with_LOC, File_Name='second_with_LOC.html')