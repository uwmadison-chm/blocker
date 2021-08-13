#!/usr/bin/env python

"""
A generator for blocked randomization.
TODO: Make this better

Usage:
  blocker grouplabel_1,...,grouplabel_N block_len num_blocks

  block_len must be a multiple of the numebr of group labels
"""

import sys

import numpy as np


def main(group_labels, block_len, num_blocks):
    num_groups = len(group_labels)
    group_nums = (np.arange(num_blocks * block_len) % num_groups)
    blocked = group_nums.reshape(num_blocks, block_len)
    np.apply_along_axis(np.random.shuffle, 1, blocked)
    group_nums_shuffled = blocked.reshape(num_blocks * block_len)
    labeled = [group_labels[i] for i in group_nums_shuffled]
    print("\n".join(labeled))



if __name__ == '__main__':
    group_labels = sys.argv[1].split(",")
    block_len = int(sys.argv[2])
    num_blocks = int(sys.argv[3])
    assert block_len % len(group_labels) == 0, f"block_len must be a multiple of {len(group_labels)}"
    main(group_labels, block_len, num_blocks)
