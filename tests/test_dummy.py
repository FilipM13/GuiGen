import os

def test_nothing():
  with open('some_art.txt', 'w') as artefact:
    os.mkdir('logs')
    artefact.write('logs/logs and shit')
  pass
