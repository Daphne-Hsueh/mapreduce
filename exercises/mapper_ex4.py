#!/usr/bin/env python

# Exercise 4: only emit records for the categories
# "Computers", "Cameras" and "Video Games".
# Use together with the original (sum) reducer.py.

import sys

WANTED = ("Computers", "Cameras", "Video Games")

for line in sys.stdin:
    data = line.strip().split("\t")
    date, time, item, category, sales, payment = data

    # Filter: only pass the wanted categories to the reducer
    if category in WANTED:
        sys.stdout.write("{0}\t{1}\n".format(category, sales))
