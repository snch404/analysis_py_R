def find_sum(lst):
    # Elements at even indices
    even_pos = [lst[i] for i in range(0, len(lst), 2)]
    # Elements at odd indices
    odd_pos = [lst[i] for i in range(1, len(lst), 2)]

    # Sort both lists
    even_pos_sorted = sorted(set(even_pos), reverse=True)
    odd_pos_sorted = sorted(set(odd_pos))

    if len(even_pos_sorted) < 2 or len(odd_pos_sorted) < 2:
        print("Not enough elements to find second largest/smallest")
        return

    second_largest_even = even_pos_sorted[1]
    second_smallest_odd = odd_pos_sorted[1]

    result = second_largest_even + second_smallest_odd
    print("Sum =", result)


# Example usage
lst = [5, 2, 9, 1, 6, 7, 3, 8]
find_sum(lst)
