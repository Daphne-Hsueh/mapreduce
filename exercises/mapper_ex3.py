#!/usr/bin/env python

# Exercise 3: raise an error when a line does NOT contain exactly six elements.

import sys

for line in sys.stdin:
    data = line.strip().split("\t")

    # Validate the record: it must have exactly six fields
    if len(data) != 6:
        raise ValueError(
            "Expected 6 elements but got {0}: {1}".format(len(data), data)
        )

    date, time, item, category, sales, payment = data
    sys.stdout.write("{0}\t{1}\n".format(category, sales))
