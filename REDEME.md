<h1>Expand Library of <i>The Farmer Was Relpaced</i></h1>

Just copy all the file into your save folder to use it.
Also you can install this libray by excuting `pip install TFWR-expand`.

Enjoy it!

# Document

Basically, `__builtin__.py`, `__init__.py` and `_tfwr_official_provided.__builtins__.py` provide the *Python* language features to you.
They are *Python* scripts which **can't** be imported in the game.

## Algorithms

`import algorithms`.

### Quick Sort

Calling `algorithms.qsort(arr)` with any `list` will sort it.

For example:
```python
from algorithms import qsort

arr = [3, -1, 11, 0, 7]

qsort(arr)

print(arr)  # [-1, 0, 3, 7, 11]
```
