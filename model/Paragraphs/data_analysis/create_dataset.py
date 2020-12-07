import os
import sys

##
os.chdir('../../..')
del(sys.path[0])
sys.path.insert(0, os.getcwd())
##

import json
import pandas as pd
import time
df = pd.DataFrame(columns=['is_Date', 'day', 'month', 'year', 'first_in_paros', 'is_First'])


with open('model/Paragraphs/data_analysis/data/saved_json.txt') as file:
    m = json.load(file)
    count = len(m)
    ind = 0
    sum_time = 0
    for key, value in m.items():
        start_time = time.time()
        for Paragraph in value['Paragraphs']:
            is_first = True
            for wrap_date in Paragraph['dates']:
                date = wrap_date['Date']
                if (date['type'] == 'DateRange'):
                    df.loc[df.shape[0]] = [False, None, None, None, wrap_date['first_in_paros'], is_first]
                else:
                    df.loc[df.shape[0]] = [True, date['day'], date['month'], date['year'], wrap_date['first_in_paros'], is_first]
                is_first = False
        ind += 1
        sum_time += (time.time() - start_time)
        print((ind / count) * 100, '%')
        print('Avg_time: ', sum_time / ind)
        print('Exc_time: ', (time.time() - start_time))
        print('Estemated_left_time: ', (count - ind) * ((sum_time / ind) / 60), 'm')
    df.to_csv('model/Paragraphs/data_analysis/data/dates.csv', index=False)





