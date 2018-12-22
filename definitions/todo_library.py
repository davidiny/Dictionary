import requests

def _url(path):
    return 'https://www.wordnik.com/words' + path


def get_word(word):
    return requests.get(_url('/{}'.format(word)))
def describe_task(id):
    return requests.get(_url('/tasks/{:d}')).format(id)
def add_task(summary, description=""):
    return requests.post(_url('/tasks'), json={'summary': summary, 'description': description})
def task_done(id):
    return requests.delete(_url('/tasks/{:d}').format(id))
def update_task(id, summary, description):
    return requests.put(_url('/tasks/{:d}').format(id), json={'summary': summary, 'description': description})

