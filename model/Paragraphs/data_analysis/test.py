import os
import sys

##
os.chdir('../../..')
del(sys.path[0])
sys.path.insert(0, os.getcwd())
##

import json
import copy

# with open('model/Paragraphs/data_analysis/data/saved_json.txt') as file:
#     m = json.load(file)
#     for key, value in m.items():
#         for Paragraph in value['Paragraphs']:
#             prev_date = {'start': 0, 'stop': 0}
#             for date in Paragraph['dates']:
#                 if (date['span']['start'] < prev_date['start']):
#                     raise NameError('Incorrect order')
#                 prev_date = copy.copy(date['span'])
