pipetools
=========


Going to:

```
$ cat file.txt | python -m pipetools 'str.split | str.lower | groupby(x => x[0])'
```

```
import re
from functools import partial
from pipetools import List, groupby, sort, select

with open('file.txt') as fo:
    array = List(fo.readlines())

only_alpha = partial(re.sub, '\W', '')

count = lambda sequence: len(sequence)

items = array | str.lower | only_alpha | groupby(count) | sort(lambda item: item[1], reverse=True) | select(lambda x: x[1] > 1)

for word, cnt in items:
    print word, cnt

```
