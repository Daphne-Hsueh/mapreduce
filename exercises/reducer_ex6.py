#!/usr/bin/env python

# Exercise 6: calculate the AVERAGE sales per category.
# average = sum of sales / number of purchases
# Use together with mapper_ex1.py (emits category as key).

import sys

sum_of_values = 0.0
count = 0
previous_key = None

for line in sys.stdin:
    data = line.strip().split("\t")
    key, value = data

    if previous_key is not None and previous_key != key:
        # Emit the average for the previous key
        average = sum_of_values / count
        sys.stdout.write("{0}\t{1}\n".format(previous_key, average))
        sum_of_values = 0.0
        count = 0

    sum_of_values += float(value)
    count += 1
    previous_key = key

# Write the last result
average = sum_of_values / count
sys.stdout.write("{0}\t{1}\n".format(previous_key, average))
