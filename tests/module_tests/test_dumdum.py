import os

def test_pass():
  os.mkdir('logs-module')
  with open('logs-module/some_art.txt', 'w') as artefact:
    artefact.write('test got errORRRRREEEEEEEE!')
  raise Exception('REEEEEEE!!!')
