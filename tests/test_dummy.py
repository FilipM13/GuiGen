import os

def test_nothing():
  with open('some_art.txt', 'w') as artefact:
    os.mkdir('logs')
    artefact.writable('logs/logs and shit')
  pass
