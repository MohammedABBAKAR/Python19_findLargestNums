# Find the Largest Numbers in a Group of Arrays

# Create a function that takes an array of arrays with numbers. 
# Return a new (single) array with the largest numbers of each.
# Examples

# findLargestNums([[4, 2, 7, 1], [20, 70, 40, 90], [1, 2, 0]]) ➞ [7, 90, 2]

# findLargestNums([[-34, -54, -74], [-32, -2, -65], [-54, 7, -43]]) ➞ [-34, -2, 7]

# findLargestNums([[0.4321, 0.7634, 0.652], [1.324, 9.32, 2.5423, 6.4314], [9, 3, 6, 3]]) ➞ [0.7634, 9.32, 9]


def findLargestNums(arr):
    # Initialize an empty list to store the largest numbers
    largest_nums = []
    
    # Iterate over each sub-array in the main array
    for sub_array in arr:
        # Find the largest number in the current sub-array and append it to the result list
        largest_nums.append(max(sub_array))
    
    # Return the list of largest numbers
    return largest_nums

# Test cases
print(findLargestNums([[4, 2, 7, 1], [20, 70, 40, 90], [1, 2, 0]]))  # ➞ [7, 90, 2]
print(findLargestNums([[-34, -54, -74], [-32, -2, -65], [-54, 7, -43]]))  # ➞ [-34, -2, 7]
print(findLargestNums([[0.4321, 0.7634, 0.652], [1.324, 9.32, 2.5423, 6.4314], [9, 3, 6, 3]]))  # ➞ [0.7634, 9.32, 9]
