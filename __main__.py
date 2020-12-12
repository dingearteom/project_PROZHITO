import sys
import os

### Changing sys and current working directory
folder_path = '/'.join(os.path.realpath(__file__).split('/')[:-1])
folder_name = folder_path.split('/')[-1]


if (sys.path[0] != folder_path):
    os.chdir(os.getcwd() + f"/{folder_name}")
    sys.path[0] += f'/{folder_name}'
###


import json
from model.model import Model
from tags_extraction.DOC import DOC
from Span import select_spans
import time

# file_name = "data/Новая разметка/Непорожний П.С .Энергетика страны глазами министра _ Дневники/Артёмова РГГУ ФК 2 курс практика Непорожний П.С. 1959-1966.docx"
# d = DOC(file_name, tags_deletion=True)

text = input()

model = Model()

doc = model.fit(text)


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
                              'mention': text[per.span.start:per.span.stop]

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
            'mention': text[per.span.start:per.span.stop]
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

id_par = [-1 for i in range(len(doc.paragraphs))]

ind = 0
for id in range(len(doc.paragraphs)):
    par = doc.paragraphs[id]
    while (ind < len(doc.locations) and doc.locations[ind].span.stop <= par.span.stop):
        id_par[ind] = id
        ind += 1

ind = 0
for location in doc.locations:
    output['Locations'].append({
        'start': location.span.start,
        'stop': location.span.stop,
        'name': location.text,
        'id': id_par[ind]
    })
    ind += 1

print(json.dumps(output, indent=4, ensure_ascii=False))
# with open('data/result.txt', 'w') as file:
#     json.dump(output, file, indent=4, ensure_ascii=False)
