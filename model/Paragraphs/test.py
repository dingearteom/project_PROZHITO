import os
import sys

##
os.chdir("../..")
del(sys.path[0])
sys.path.insert(0, os.getcwd())
##

import json
from slovnet.markup import SpanMarkup
from tags_extraction.DOC import DOC
from model.Paragraphs.classification import Type_of_Text
from model.Paragraphs.Paragraphs import Paragraphs_Ext
from evaluation.render import render_box_markup
import gc

def save_types_of_docs():
    blacklist = []
    with open("model/data/blacklist.txt") as file:
        blacklist = json.load(file)

    num_of_doc = 0
    with open('model/data/main_file.txt') as file:
        main_file = json.load(file)

        for key, value in main_file.items():
            for file_name in value:
                if (file_name in blacklist):
                    continue
                num_of_doc += 1
    print(num_of_doc)

    with open('model/data/main_file.txt') as file:
        main_file = json.load(file)

        type = {}
        ind = 0
        for key, value in main_file.items():
            for file_name in value:
                if (file_name in blacklist):
                    continue
                ind += 1
                d = DOC(file_name)
                cl = Type_of_Text()
                type[file_name] = cl.fit(d.text)
                print((ind / num_of_doc) * 100, '%')
            gc.collect()
        with open('model/Paragraphs/data/type.txt', 'w') as file_type:
            json.dump(type, file_type, ensure_ascii=False, indent=4)

def render_par():
    blacklist = []
    with open("model/data/blacklist.txt") as file:
        blacklist = json.load(file)

    num_of_doc = 0
    with open('model/data/main_file.txt') as file:
        main_file = json.load(file)

        for key, value in main_file.items():
            for file_name in value:
                if (file_name in blacklist):
                    continue
                num_of_doc += 1
    print(num_of_doc)

    with open('model/data/main_file.txt') as file:
        main_file = json.load(file)

        ind = 0
        for key, value in main_file.items():
            file_num = 0
            map_file = {}
            for file_name in value:
                if (file_name in blacklist):
                    continue
                print(file_name)
                file_num += 1
                ind += 1
                d = DOC(file_name)
                par_ext = Paragraphs_Ext()
                paragraphs = par_ext.fit(d.text)

                if (not os.path.exists(f"model/Paragraphs/data/render_Paragraphs/{key}")):
                    os.system(f"mkdir model/Paragraphs/data/render_Paragraphs/\"{key}\"")
                if (not os.path.exists(f"model/Paragraphs/data/render_Paragraphs/{key}/Paragraphs{file_num}.html")):
                    os.system(f"touch model/Paragraphs/data/render_Paragraphs/\"{key}\"/Paragraphs{file_num}.html")

                map_file[file_name] = file_num
                render_box_markup(SpanMarkup(d.text, paragraphs), File_Name=f"model/Paragraphs/data/render_Paragraphs/{key}/Paragraphs{file_num}.html")


                print((ind / num_of_doc) * 100, '%')
            if (file_num > 0):
                with open(f"model/Paragraphs/data/render_Paragraphs/{key}/sources.txt", 'w') as file_sources:
                    json.dump(map_file, file_sources, ensure_ascii=False, indent=4)

            gc.collect()


if __name__ == '__main__':
    render_par()
    #save_types_of_docs()
    # file_name = "data/Новая разметка/Шеварднадзе Э._Когда рухнул железный занавес/Э Шеварднадзе.docx"
    # d = DOC(file_name)
    # cl = Type_of_Text()
    # cl.fit(d.text)
    # with open('model/Paragraphs/data/type.txt') as file:
    #     type = json.load(file)
    #     for key, value in type.items():
    #         print(key, value)
