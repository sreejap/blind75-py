arr.sort()                 # in-place ascending
arr.sort(reverse=True)     # descending
sorted(arr)                # returns new sorted list

# custom key
arr.sort(key=lambda x: x[1])

In Python, you can use list.sort() to sort the content of the list in-place, or sorted(list) to return a new list containing the sorted list. They are both stable sorts. Python uses Timsort, which uses merge sort for larger data and insertion sort for smaller data.
