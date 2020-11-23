from collections import Counter
import pprint

pp = pprint.PrettyPrinter()

#  Calculates next row of Pascal's triangle based on previous row
def calculate_next_row(curr_row):
    if curr_row == []:
        return [1]
    next_row = [1]
    for r in range(1, len(curr_row)):
        next_row.append(curr_row[r] + curr_row[r - 1])
    next_row.append(1)
    return next_row


# Generatest Pascal's triangle up to n rows
def pascal_gen(n):
    pascal_triangle = [[1]]
    while len(pascal_triangle[-1]) < n:
        pascal_triangle.append(calculate_next_row(pascal_triangle[-1]))
    return pascal_triangle


# User input
n = int(input("How many rows? "))
min_freq = int(input("Minimum frequency? "))

pascals_triangle = pascal_gen(n)
# pp.pprint(pascals_triangle)
counts = Counter(
    num 
    for row in pascals_triangle
    for num in row
)

threshold_counts = {}  # Table of counts above the minimum requirement

for (num, count) in counts.items():
    new_count = count + 2 if n < num else count  # It'll appear 2 more times when row==num
    if new_count >= min_freq:
        threshold_counts[num] = new_count

pp.pprint(threshold_counts)
