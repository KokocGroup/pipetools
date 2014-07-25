pipetools
=========


Going to:

```
$ cat file.txt | python -m pipetools 'str.split | str.lower | groupby(count) | ... '
```

Current Example of code:

```
import re
from functools import partial
from pipetools import List, groupby, sort, select

with open('file.txt') as fo:
    array = List(fo.readlines())

only_alpha = partial(re.sub, '\W', '')

count = lambda sequence: len(sequence)

items = array | str.lower | only_alpha | groupby(count) | sort(lambda (word, cnt): cnt, reverse=True) | select(lambda x: x[1] > 1)

for word, cnt in items:
    print word, cnt

```
