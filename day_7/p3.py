# Rotate list elements to the right by one position
def rotate_list(lst):
    if len(lst) == 0:
        return lst
    
    # Store the last element
    last = lst[-1]
    
    # Shift elements one step to the right
    for i in range(len(lst) - 1, 0, -1):
        lst[i] = lst[i - 1]
    
    # Place last element at the first position
    lst[0] = last
    
    return lst

# Example usage
lst = [10, 20, 30, 40, 50]
print("Original List:", lst)
rotated_lst = rotate_list(lst)
print("Rotated List :", rotated_lst)
