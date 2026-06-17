#!/usr/bin/env python

# Exercise 1: emit (category, sales) instead of (payment, sales)
# so the reducer sums the sales per CATEGORY.

import sys

for line in sys.stdin:
    data = line.strip().split("\t")
    date, time, item, category, sales, payment = data
    # Key is the category, value is the sales
    sys.stdout.write("{0}\t{1}\n".format(category, sales))
