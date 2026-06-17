#!/usr/bin/env python

# Exercise 2: count the NUMBER of purchases per key (category),
# instead of summing the sales.
# Use together with mapper_ex1.py (emits category as key).

import sys

count = 0
previous_key = None

for line in sys.stdin:
    data = line.strip().split("\t")
    key, value = data

    if previous_key is not None and previous_key != key:
        # New key starts: emit count for the previous key
        sys.stdout.write("{0}\t{1}\n".format(previous_key, count))
        count = 0

    # Count this purchase (the value/sales is ignored)
    count += 1
    previous_key = key

# Write the last result
sys.stdout.write("{0}\t{1}\n".format(previous_key, count))
