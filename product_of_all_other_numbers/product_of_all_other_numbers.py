'''
Input: a List of integers
Returns: a List of integers
'''

def product_of_all_other_numbers(arr):
    arr_len = len(arr)
    left_product = [1] * arr_len
    right_product = [1] * arr_len
    product = [1] * arr_len
    
    if arr_len == 0:
        return None
    if arr_len == 1:
        return arr
    # Store left products so that the last element will be the product of all elements to the right of it
    i = 1
    while i < arr_len:
        left_product[i] = arr[i - 1] * left_product[i - 1]
        i += 1
    # Store left products so that the last element will be the product of all elements to the right of it
    i = arr_len - 2
    while i >= 0:
        right_product[i] = arr[i + 1] * right_product[i + 1]
        i -= 1
    # Build the product array
    i = 0
    while i < arr_len:
        product[i] = left_product[i] * right_product[i]
        i += 1

    return product


if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [1, 2, 3, 4, 5]
    arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
