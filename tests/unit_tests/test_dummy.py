import os

def test_nothing():
  os.mkdir('logs-unit')
  with open('logs-unit/some_art.txt', 'w') as artefact:
    artefact.write('logs and shit')
  pass
