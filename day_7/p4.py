def calculate_mean(lst):
    return sum(lst) / len(lst)


def calculate_median(lst):
    sorted_lst = sorted(lst)
    n = len(sorted_lst)
    mid = n // 2

    if n % 2 == 0:  # even count → average of two middle values
        return (sorted_lst[mid - 1] + sorted_lst[mid]) / 2
    else:  # odd count → middle value
        return sorted_lst[mid]


def calculate_mode(lst):
    frequency = {}
    for num in lst:
        frequency[num] = frequency.get(num, 0) + 1

    max_freq = max(frequency.values())
    modes = [key for key, value in frequency.items() if value == max_freq]

    if len(modes) == len(frequency):  # all numbers appear equally
        return "No mode"
    return modes


# Example usage
numbers = [4, 2, 7, 4, 9, 2, 4, 6]

print("Numbers:", numbers)
print("Mean  =", calculate_mean(numbers))
print("Median=", calculate_median(numbers))
print("Mode  =", calculate_mode(numbers))
