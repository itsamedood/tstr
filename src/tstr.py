from io import StringIO
from random import randint
from re import findall


def rm_char(_charset: str, _char: str) -> str:
  """ Removes first `_char` from `_charset`. So if there's 2 `l`s, one will still be present. """

  new_charset = StringIO()
  found = False

  for c in _charset:
    # If c is char to remove but we found it already, or c is not the char to remove, write it.
    if (c == _char and found) or not c == _char:
      new_charset.write(c)
    else:  # Else, skip it and set found to true. This allows this function to work for a string like `Hello` with 2 of the same letter in it.
      found = True

  return new_charset.getvalue()


def rearrange(_str: str) -> str:
  """ Rearranges the letters of `_str[1:-1]` """

  result = StringIO()  # Start with 1st letter.
  resstr = ''
  charset = (excluded:=_str[1:-1])  # Exclude first and last letter. Seperate variables for clarity.

  for l in excluded:
    if l.isalpha():
      # Rearrange letters randomly, not allowing the same character to be put in the same spot.
      result.write(rl:=charset[randint(0, len(charset)-1)])
      charset = rm_char(charset, rl)

    resstr = result.getvalue()

  return f"{_str[0]}{resstr}{_str[-1]}"


def tstr(_str: str) -> str:
  """ Converts `_str` to a [Typoglycemia](https://www.dictionary.com/e/typoglycemia/) string. """
  # \b = word Boundary, a position between a word and non-word character.
  words: list[str] = findall(r"\b[a-zA-Z]+\b", _str)
  final_words: list[str] = []

  for word in words:
    if len(word) > 3:  # Prevents the loop below from being infinite given something like 'the'.
      # Ensure that the string is not the same, which are pretty low odds but still.
      while (reword:=rearrange(word)) == word:
        continue

      final_words.append(reword)  # Just like `words` but each word has been rearranged.
    else:
      final_words.append(word)

  # We're done using `_str` and can modify it to save an extra variable.
  for i, fword in enumerate(final_words):
    _str = _str.replace(words[i], fword)

  return _str
