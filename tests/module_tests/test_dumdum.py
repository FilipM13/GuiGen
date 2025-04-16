from gui_gen import App, Process, arguments
from time import sleep
from datetime import datetime

def test_1():
  def my_proc(
      a1: arguments.Argument,
      a2: arguments.Float,
      a3: arguments.Int,
      a4 = 1
  ):
      sleep(10)
      return datetime.now()

  pr = Process(
      my_proc
  )

  class CustomRegex(arguments.Regex):
      pattern = r'[\d]*'

  def my_proc2(
      a1: arguments.Argument,
      a2: arguments.Float,
      text: CustomRegex,
      ch1: arguments.Choice,
      ch2: arguments.Choice = [1, 2, 3],
      d: arguments.Date = datetime(2021, 3, 7).date(),
      dt: arguments.DateTime = datetime(2021, 1, 12, 10, 21),
      a3: arguments.Int = 2,
      a4: arguments.Boolean = False,
      a5: arguments.Boolean = True
  ):
      '''
      stuff
      '''
      print(ch1)
      print(ch2)
      return datetime.now()

  pr2 = Process(
      my_proc2,
      name='Custom name!'
  )

  a = App(
      processes=[pr, pr2],
      primary_colour='navy',
      secondary_colour='darkgray',
      accent_colour='lime',
      background_colour='black'
  )

  a.build()
  pass