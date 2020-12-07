import os
import sys

##
os.chdir("../../..")
del(sys.path[0])
sys.path.insert(0, os.getcwd())
##

import pandas as pd
from model.Paragraphs.data_analysis.doc import DOC as DOC_with_time
import json

blacklist = []
with open("model/data/blacklist.txt") as file:
    blacklist = json.load(file)


num_doc = 0
with open('model/data/main_file.txt') as file:
    main_file = json.load(file)
    for key, value in main_file.items():
        for file_name in value:
            if (file_name in blacklist):
                continue
            num_doc += 1

df = pd.DataFrame(columns=['file_name'] + [i for i in range(1 << 7)])


with open("model/data/main_file.txt") as file:
    main_file = json.load(file)
    ind = 0
    for key, value in main_file.items():
        for file_name in value:
            if (file_name in blacklist):
                continue
            print(file_name)
            d = DOC_with_time(file_name=file_name)

            arr = [0 for i in range(1 << 7)]
            num_dates = 0

            for Paragraph in d.Paragraphs:
                num_dates += len(Paragraph.dates)
                for wrap_date in Paragraph.dates:
                    date = wrap_date.Date
                    arr[date.to_num()] += 1
            for i in range(1 << 7):
                arr[i] = arr[i] / num_dates

            df.loc[df.shape[0]] = [file_name] + arr
            ind += 1
            print((ind / num_doc) * 100, '%')

df.to_csv('model/Paragraphs/data_analysis/data/dates_clusterisation.csv')






