import sys
import os

### Changing sys and current working directory
if (sys.path[0].split('/')[-1] != 'project'):
    os.chdir(os.getcwd() + "/project")
    sys.path[0] += '/project'
###


import json
from model.model import Model
from tags_extraction.DOC import DOC
from Span import select_spans
import time

file_name = "data/Новая разметка/Непорожний П.С .Энергетика страны глазами министра _ Дневники/Артёмова РГГУ ФК 2 курс практика Непорожний П.С. 1959-1966.docx"
d = DOC(file_name, tags_deletion=True)

model = Model()

doc = model.fit(d.text)


output = {
    "Persons": [],
    "Persons_Full_Name": {},
    "Persons_Full_Set_of_Mentions": {},
    "Paragraphs": [],
    "Locations": []
}

for per in doc.per:
    output['Persons'].append({'id': per.id,
                              'start': per.span.start,
                              'stop': per.span.stop,
                              'mention': d.text[per.span.start:per.span.stop]

    })

ids = []
for per in doc.per:
    ids.append(per.id)

for id in ids:
    output['Persons_Full_Name'][id] = {'Nickname': '-',
                                       'Name': '-',
                                       'Surname': '-',
                                       'Patronymic': '-'
                                       }


for id in ids:
    output['Persons_Full_Set_of_Mentions'][id] = []

for per in doc.per:
    output['Persons_Full_Set_of_Mentions'][per.id].append(
        {   'start': per.span.start,
            'stop': per.span.stop,
            'mention': d.text[per.span.start:per.span.stop]
         }
    )

for par in doc.paragraphs:
    locations = []
    for location in par.Locations:
        locations.append(location.text)
    output['Paragraphs'].append({
        'start': par.span.start,
        'stop': par.span.stop,
        'start_time': (0, 0, 0),
        'stop_time': (0, 0, 0),
        'locations': locations
    })

for location in doc.locations:
    output['Locations'].append({
        'start': location.span.start,
        'stop': location.span.stop,
        'name': location.text
    })

with open('data/result.txt', 'w') as file:
    json.dump(output, file, indent=4, ensure_ascii=False)
