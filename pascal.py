import pprint

pp = pprint.PrettyPrinter()


def calculate_next_row(curr_row):
    if curr_row == []:
        return [1]
    next_row = [1]
    for r in range(1, len(curr_row)):
        next_row.append(curr_row[r] + curr_row[r-1])
    next_row.append(1)
    return next_row


def pascal_gen(n):
    pascal_triangle = [[1]]
    while len(pascal_triangle[-1]) < n:
        pascal_triangle.append(calculate_next_row(pascal_triangle[-1]))
    return pascal_triangle


def count_number_frequencies(triangle):
    frequency_table = {}

    def count_list(input_list):
        for item in input_list:
            if isinstance(item, list):
                count_list(item)
            else:
                if item in frequency_table.keys():
                    frequency_table[item] += 1
                else:
                    frequency_table[item] = 1
    count_list(triangle)
    return frequency_table


n = int(input("How many rows? "))
min_freq = int(input("Minimum frequency? "))

triangle = pascal_gen(n)
# print(triangle)
counts = count_number_frequencies(triangle)

threshold_counts = {}

for (num, count) in counts.items():
    new_count = count
    if num > n:
        new_count += 2  # It'll appear 2 more times in its own row
    if new_count >= min_freq:
        threshold_counts[num] = new_count

# print(counts)

pp.pprint(threshold_counts)
