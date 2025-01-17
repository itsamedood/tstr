from io import StringIO
from random import randint
from re import findall


class TypoglycemiaEngine:
  """ Core of the program, actually responsible for modifying the given text. """

  LOOP_MAX = 100  # Max amount of times the engine should try rearranging whatever word it's on.

  def __init__(self) -> None:
    ...

  def rm_char(self, _mchars: str, _char: str) -> str:
    """ Removes first `_char` from `_charset`. So if there's 2 `l`s, one will still be present. """

    new_mchars = StringIO()
    found = False

    for c in _mchars:
      # If c is char to remove but we found it already, or c is not the char to remove, write it.
      if (c == _char and found) or not c == _char:
        new_mchars.write(c)
      # Else, skip it and set found to true. This allows this function to work for a string like `Hello` with 2 of the same letter in it.
      else:
        found = True

    return new_mchars.getvalue()

  def rearrange(self, _text: str) -> str:
    """ Rearranges the letters of `_str[1:-1]` """

    result = StringIO()
    mchars = _text[1:-1]

    for c in mchars:
      if c.isalpha():
        # Rearrange letters randomly, not allowing the same character to be put in the same spot.
        result.write(rc:=mchars[randint(0, len(mchars)-1)])
        mchars = self.rm_char(mchars, rc)

    return f"{_text[0]}{result.getvalue()}{_text[-1]}"

  def convert(self, _text: str) -> str:
    """ Converts `_str` to a [Typoglycemia](https://www.dictionary.com/e/typoglycemia/) string. """

    # \b = word Boundary, a position between a word and non-word character.
    text = _text
    words: list[str] = findall(r"\b[a-zA-Z]+\b", text)
    final_words: list[str] = []
    tries = 0

    for word in words:
      if len(word) > 3:  # Prevents the loop below from being infinite given something like 'the'.
      # Ensure that the string is not the same, which are pretty low odds but still.
        while ((reword:=self.rearrange(word)) == word) or tries >= self.LOOP_MAX:
          tries += 1
          continue

        final_words.append(reword)  # Just like `words` but each word has been rearranged.
      else:
        final_words.append(word)

    for i, fword in enumerate(final_words):
      text = text.replace(words[i], fword)

    return text

  def shell(self) -> None:
    print("!exit to exit this shell.")

    while 1:
      text = input("> ")
      if text == "!exit":
        break

      print(self.convert(text))
