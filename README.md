<h1>Expand Library of <i>The Farmer Was Relpaced (TFWR)</i></h1>

Just copy all the file into your save folder to use it.
Also you can install this libray by excuting `pip install TFWR-expand`.

**CAUTION: Remember to backup a `__builtin__.py` file in your save folder before using this library. This library will overwrite the original `__builtin__.py` provided by *The Farmer Was Replaced* official. Or, you can use this libray at other folder or do not copy `__builtin__.py` file into your save folder.** By the way, you can find `_tfwr_official_provided.__builtins__.py` in this library. It is a copy of the original `__builtin__.py` file provided by *The Farmer Was Replaced* official.

Enjoy it!

# Document

Basically, `__builtin__.py`, `__init__.py` and `_tfwr_official_provided.__builtins__.py` provide the *Python* language features to you.
They are *Python* scripts which **can't** be imported in the game.

## algorithms

`import algorithms`.

### `qsort(arr)`

Calling `algorithms.qsort(arr)` with any `list` will sort it.

For example:
```python
from algorithms import qsort

arr = [3, -1, 11, 0, 7]

qsort(arr)

print(arr)  # [-1, 0, 3, 7, 11]
```

## tools

`import tools`.

### `has_item(item)`

Calling `tools.has_item(item)` for checking whether player has `Items`. Returns `True` if the player has it, otherwise `False`.

### `cost_enough(entity, level=None, scale=1.0)`

Calling `tools.cost_enough(thing, level=None, scale=1.0)` for checking whether player has enough item(s) to buy or plant the `thing`. Returns `True` if the player has enough item(s), otherwise `False`.
