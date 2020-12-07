
import os
import sys

## change of current working directory and sys path
os.chdir('../..')
del(sys.path[0])
sys.path.insert(0, os.getcwd())
##

from pullenti_client import Client
from slovnet.span import Span
from tags_extraction.DOC import DOC
from model.Dates.dates import Dates
import docker
import time
import subprocess


# environment = os.environ
# print(environment.get('DOCKER_HOST'))
#
# print(docker)
# print(os.environ['DOCKER_HOST'])
# for key, value in os.environ.items():
#     print(key, value)

# client = docker.from_env()
#
# for container in client.containers.list(all=True):
#     if (container.attrs['Name'] == '/pullenti'):
#         container.remove(force=True)


# client = docker.from_env()

# for container in client.containers.list(all=True):
#     if (container.attrs['Name'] == '/pullenti'):
#         container.remove(force=True)

# client.containers.run('pullenti/pullenti-server', detach=True, name='pullenti', ports={'8080': 8083},
#                       volumes={f'{os.getcwd()}/data/custom.xml' : {'bind' : '/app/conf.xml'}})


file_name = "data/Новая разметка/Шеварднадзе Э._Когда рухнул железный занавес/Э Шеварднадзе.docx"

d = DOC(file_name=file_name)
Dates_extractor = Dates()

# client = Client('localhost', 8083)
# res = client(d.text)
# print(res)
# dates = Dates_extractor.fit(d.text)
#
# for date in dates:
#     print(date, d.text[date.span.start:date.span.stop])