'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
# Alternative solution
#def single_number(arr):
#    result = 0
#    for i in arr:
#        result ^= i
#    return result

def single_number(arr):
    # Your code here
    number_counts = {}
    unique_number = 0

    arr_len = len(arr)
    i = 0
    while i < arr_len:
        number = arr[i]

        if number in number_counts:
            if number_counts[number]:
              number_counts[number] = False
              unique_number -= number
        else:
          number_counts[number] = True
          unique_number += number
        i += 1
    return unique_number


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")
