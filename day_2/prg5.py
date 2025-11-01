def find_min_max(*args):
    mv = mxv = args[0]
    for num in args:
        if num < mv:
            mv = num
        if num > mxv:
            mxv = num
    return mv, mxv
a= [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
mv, mxv = find_min_max(*a)
print("Minimum value:", mv)
print("Maximum value:", mxv)
b= [10, 20, 30, 40, 50]
mv_b, mxv_b = find_min_max(*b)
print("Minimum value:", mv_b)
print("Maximum value:", mxv_b)