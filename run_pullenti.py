import docker
import os
import time

client = docker.from_env()

for container in client.containers.list(all=True):
    if (container.attrs['Name'] == '/pullenti'):
        container.remove(force=True)


client.containers.run('pullenti/pullenti-server', detach=True, name='pullenti', ports={'8080': 8083},
                      volumes={f'{os.getcwd()}/data/custom.xml': {'bind': '/app/conf.xml'}})

