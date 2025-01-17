from sys import argv
from tstr import tstr


# The program name is centered, that's why there's 10 spaces before it.
USAGE_STR = """
  +------------------------------------------------------------------+
  | Typoglycemia String \033[4;1;30m(https://www.dictionary.com/e/typoglycemia/)\033[0;0;0m |
  | Usage: tstr <text>                                               |
  | Example: tstr Hello, world!                                      |
  +------------------------------------------------------------------+
"""


if __name__ == "__main__":
  print(tstr(' '.join(argv[1:])) if len(argv) > 1 else USAGE_STR)
