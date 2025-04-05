import os

def test_nothing():
  os.mkdir('logs')
  with open('logs/some_art.txt', 'w') as artefact:
    artefact.write('logs and shit')
  pass
