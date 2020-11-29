from tags_extraction.DOC import DOC
from evaluation.statistics import evaluate, statistics
from evaluation.render import render_box_markup
from slovnet.markup import SpanMarkup
from Span import select_spans
from model.model import Model, fit_time
from guppy import hpy
import json
import time
import os
import gc
import dateparser
import sys
import os

## change of the current working directory and sys path
os.chdir('..')
del(sys.path[0])
##

def full_render_of_the_model():
    model = Model()
    res = statistics()

    num_of_doc = 0

    with open('model/data/main_file.txt') as file:
        main_file = json.load(file)
        for key, value in main_file.items():
            for file_name in value:
                num_of_doc += 1
    print(num_of_doc)




    with open('model/data/main_file.txt') as file:
        main_file = json.load(file)
        ind = 0
        sum_duration = 0

        for key, value in main_file.items():
            for file_name in value:
                print(file_name)

                start_time = time.time()

                d = DOC(file_name=file_name)
                spans_model = model.fit(d.text)
                markup_per = SpanMarkup(d.text, select_spans(spans_model, ['PER']))

                if (not os.path.exists(f"model/data/render_results/{key}/compare.html")):
                    os.system(f"touch model/data/render_results/\"{key}\"/compare.html")

                render_box_markup(SpanMarkup(d.text, d.per), markup_per, File_Name=f"model/data/render_results/{key}/compare.html")

                st = evaluate(d.per, markup_per.spans)

                with open(f"model/data/render_results/{key}/statistics.txt", 'w') as file:
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
            gc.collect()

    print(res)

    with open("model/data/statistics.txt", 'w') as file:
        file.write(res.__str__())

if __name__ == "__main__":
    file_name = "data/Новая разметка/Непорожний П.С .Энергетика страны глазами министра _ Дневники/Артёмова РГГУ ФК 2 курс практика Непорожний П.С. 1959-1966.docx"
    d = DOC(file_name=file_name)

    print(fit_time(d.text[:1000]))

    #render_box_markup(SpanMarkup(d.text, spans), File_Name="model/data/Test/time.html")
