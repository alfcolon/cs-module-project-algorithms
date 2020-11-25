'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k):
    rows = len(nums) - k + 1
    max_nums = [None] * rows
    max_nums_index = 0
    start_index = 0
    end_index = k - 1
    while start_index <= end_index and end_index < len(nums):
        number = nums[start_index]
        if max_nums[max_nums_index] == None:
            max_nums[max_nums_index] = number
        elif max_nums[max_nums_index] < number:
            max_nums[max_nums_index] = number
        if start_index == end_index:
            if max_nums_index < rows:
                max_nums_index += 1
                start_index = max_nums_index
                end_index = start_index + k - 1
        else:
            start_index += 1
    return max_nums

if __name__ == '__main__':
     Use the main function here to test out your implementation
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
