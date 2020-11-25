'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # Your code here
    zero_index = -2
    
    i = 0
    while i < len(arr):
        # Break early when the index reaches the sorted zeroes
        # minus one
        if i == zero_index or i == zero_index - 1:
            break
        if arr[i] == 0:
            if zero_index == -2:
                zero_index = len(arr) - 1
            # handling edge case for array full of zeroes
            # with the zero_index >= 0 check
            while arr[zero_index] == 0 and zero_index >= 0:
                zero_index -= 1
            # handling array that's already sorted
            if zero_index == 0:
                break
            arr[i] = arr[zero_index]
            arr[zero_index] = 0
        i += 1
    return arr

if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")
