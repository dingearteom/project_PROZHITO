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

filename = input()
model = Model()

d = DOC(file_name=filename)
spans_module = select_spans(model.fit(d.text), ['PER'])

output = {
    "Persons": [],
    "Persons_Full_Name": {},
    "Persons_Full_Set_of_Mentions": {},
    "Paragraphs": [],
    "Locations": []
}

for span in spans_module:
    output['Persons'].append({'id': 0, 'start' : span.start, 'stop' : span.stop, 'mention': d.text[span.start: span.stop]})
print(json.dumps(output, ensure_ascii=False).encode('utf-8').decode())
