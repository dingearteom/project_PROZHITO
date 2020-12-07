import os
import sys

## Changing of current working directory and sys path
os.chdir("../../..")
del(sys.path[0])
sys.path.insert(0, os.getcwd())
##

import json
from model.Paragraphs.data_analysis.doc import DOC as DOC_with_Time
from model.Dates.dates import Dates

import gc
import time

num_of_doc = 0
with open("model/data/main_file.txt") as file:
    main_file = json.load(file)

    for key, value in main_file.items():
        for file_name in value:
            num_of_doc += 1


with open('model/data/blacklist.txt') as file:
    black_list = json.load(file)

with open("model/data/main_file.txt") as file:
    main_file = json.load(file)
    res = {}

    ind = 0
    sum_duration = 0

    for key, value in main_file.items():
        for file_name in value:
            if (file_name in black_list):
                break
            start_time = time.time()
            print(file_name)

            d = DOC_with_Time(file_name=file_name)
            res[key] = d.encode()

            ind += 1

            duration = (time.time() - start_time)
            sum_duration += duration

            print((ind / num_of_doc) * 100, "%")
            print("Estimated time left: ", ((sum_duration / ind) * (num_of_doc - ind)) / 60, 'min')
            print("Avg_duration: ", sum_duration / ind, 's')
            print("Duration: ", duration, 's')
        gc.collect()

    with open('model/Paragraphs/data_analysis/data/saved_json.txt', 'w') as json_rep:
        json.dump(res, json_rep, indent=4, ensure_ascii=False)

