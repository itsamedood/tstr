from os.path import abspath, exists, isfile
from sys import argv  #, exit
from tstr import TypoglycemiaEngine


class Cli:
  """ Handles flags and arguments. """

  USAGE_STR = """  +------------------------------------------------------------------+
  | Typoglycemia String \033[4;1;30m(https://www.dictionary.com/e/typoglycemia/)\033[0;0;0m |
  |   Usage: tstr <text> | <file-path>                               |
  |   Example: tstr Hello, world!                                    |
  |                                                                  |
  |   Run `tstr -help` for help.                                     |
  +------------------------------------------------------------------+
"""

  HELP_STR = """
  +--------------------------------------------------------+
  | Typoglycemia String Help                               |
  |                                                        |
  | Flags:                                                 |
  |   -help  -h   Displays this menu.                      |
  |   -shell -s   Lets you send text to convert endlessly. |
  +--------------------------------------------------------+
"""

  def __init__(self) -> None:
    self.engine = TypoglycemiaEngine()
    self.flags = self.get_flags()

    for flag in self.flags:
      match flag:
        case "help" | 'h':
          print(self.HELP_STR)

        case "shell" | 's':
          self.engine.shell()

        case _:
          ...
          # print("-%s is not a flag." %flag)
          # exit(1)

  def ispath(self, _arg: str) -> bool:
    """ Returns `True` if given arg exists as a path and leads to a file. """
    return exists(_arg) and isfile(_arg)

  def get_flags(self) -> list[str]:
    """ List of all args starting with `-`. """
    return [a[1:] for a in argv if a[0] == '-']

  def process(self) -> None:
    """
    Determines whether to process `argv` as text or as a file path.
    If `argv[1]` is a valid path, it takes priority over the rest of `argv`.
    """

    if len(argv) > 1:
      text = ' '.join(argv[1:])
      potential_path = argv[1]

      # For some reason, when trying to test this on `.editorconfig`, the program hangs.
      # Works on every other file including `.gitignore`, I'm so confused...
      if self.ispath(pp:=abspath(potential_path)):
        try:
          with open(pp, 'r') as file:
            print(self.engine.convert(file.read()))
        except:
          print("Failed to open %s." %pp)

      else:
        print(self.engine.convert(text))

    else:
      print(self.USAGE_STR)
