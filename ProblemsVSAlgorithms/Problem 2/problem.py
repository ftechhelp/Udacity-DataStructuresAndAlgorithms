def rotated_array_search(input_list, number):
    left_index = 0
    right_index = len(input_list) - 1

    while left_index <= right_index:
        middle_index = (left_index + right_index) // 2

        if number == input_list[middle_index]:
            return middle_index

        if input_list[left_index] <= input_list[middle_index]:

            if input_list[left_index] <= number < input_list[middle_index]:
                right_index = middle_index - 1
            else:
                left_index = middle_index + 1
        else:
            if input_list[middle_index] < number <= input_list[right_index]:
                left_index = middle_index + 1
            else:
                right_index = middle_index - 1

    return -1

def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1
    
def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])