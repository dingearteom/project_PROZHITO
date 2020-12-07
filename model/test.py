import sys
import os

## change of the current working directory and sys path
os.chdir('..')
del(sys.path[0])
sys.path.insert(0, os.getcwd())
##




from tags_extraction.DOC import DOC
from evaluation.statistics import evaluate, statistics
from evaluation.render import render_box_markup
from slovnet.markup import SpanMarkup
from model.Dates.dates import Dates
from Span import select_spans
from model.model import Model
from model.Per_and_locations_spans import Per_and_Loc
from guppy import hpy
import ru2
import json
import time
import os
import gc
import dateparser


def full_render_of_the_model_per():
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

def full_render_of_the_model_dates():

    num_of_doc = 0

    with open('model/data/main_file.txt') as file:
        main_file = json.load(file)
        for key, value in main_file.items():
            for file_name in value:
                num_of_doc += 1
    print(num_of_doc)

    with open('model/data/blacklist.txt') as file:
        blacklist = json.load(file)

    with open('model/data/main_file.txt') as file:
        main_file = json.load(file)
        ind = 0
        sum_duration = 0

        for key, value in main_file.items():
            file_num = 0
            sources = {}

            k = 0
            for file_name in value:
                if (not file_name in blacklist):
                    k += 1
            for file_name in value:
                if (file_name in blacklist):
                    continue
                file_num += 1
                print(file_name)

                start_time = time.time()

                d = DOC(file_name=file_name)
                model_time = Dates()
                spans_model = [date.span for date in model_time.fit(d.text)]

                if (not os.path.exists(f'model/data/render_dates/{key}')):
                    os.system(f"mkdir model/data/render_dates/\"{key}\"")
                sources[file_num] = file_name

                if (not os.path.exists(f"model/data/render_dates/{key}/dates{file_num}.html")):
                    os.system(f"touch model/data/render_dates/\"{key}\"/dates{file_num}.html")


                render_box_markup(SpanMarkup(d.text, spans_model), File_Name=f"model/data/render_dates/{key}/dates{file_num}.html")

                duration = (time.time() - start_time)
                sum_duration += duration

                ind += 1
                print((ind / num_of_doc) * 100, "%")
                print("Estimated time left: ", ((sum_duration / ind) * (num_of_doc - ind)) / 60, 'min')
                print("Avg_duration: ", sum_duration / ind, 's')
                print("Duration: ", duration, 's')
            if (k != 0):
                with open(f"model/data/render_dates/{key}/sources.txt", 'w') as file_sources:
                    json.dump(sources, file_sources, ensure_ascii=False)
            gc.collect()

if __name__ == "__main__":
    file_name = "data/Новая разметка/Непорожний П.С .Энергетика страны глазами министра _ Дневники/Артёмова РГГУ ФК 2 курс практика Непорожний П.С. 1959-1966.docx"
    d = DOC(file_name=file_name)
    sample_sentences = "Привет Миру! Как твои дела? Сегодня неплохая погода."
    nlp = ru2.load_ru2('ru2')
    nlp.add_pipe(nlp.create_pipe('sentencizer'), first=True)
    doc = nlp(sample_sentences)
    for s in doc.sents:
        print(list(['lemma "{}" from text "{}"'.format(t.lemma_, t.text) for t in s]))
