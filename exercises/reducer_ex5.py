#!/usr/bin/env python

# Exercise 5: count purchases per category, but only OUTPUT categories
# that have more than 114 purchases (HAVING COUNT(*) > 114).
# Use together with mapper_ex1.py (emits category as key).

import sys

count = 0
previous_key = None

for line in sys.stdin:
    data = line.strip().split("\t")
    key, value = data

    if previous_key is not None and previous_key != key:
        # Only emit the previous key if its count exceeds 114
        if count > 114:
            sys.stdout.write("{0}\t{1}\n".format(previous_key, count))
        count = 0

    count += 1
    previous_key = key

# Handle the last key
if count > 114:
    sys.stdout.write("{0}\t{1}\n".format(previous_key, count))
