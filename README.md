# blocker
A simple blocked randomization script. Requires python 3, numpy.

```
Usage:
  blocker grouplabel_1,...,grouplabel_N block_len num_blocks
  block_len must be a multiple of the numebr of group labels
```

Will generate block_len * num_blocks lines, each with one of the grouplabels on it. You're guaranteed to not have a run of more than block_len long of any group label.
