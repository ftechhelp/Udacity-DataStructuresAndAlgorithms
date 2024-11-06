def rearrange_digits(input_list: list[int]) -> tuple[int, int]:
    """
    Rearrange the digits of the input list to form two numbers such that their 
    sum is maximized.

    This function sorts the input list in descending order and then alternates 
    the digits to form two numbers.

    Args:
    input_list (list[int]): A list of integers to be rearranged.

    Returns:
    tuple[int, int]: A tuple containing two integers formed by rearranging the 
    digits of the input list.
    """

    if len(input_list) == 1:
        return (input_list[0], 0)
    
    sorted_input_list = mergesort(input_list)
    max_sum_tuple = get_max_sum_tuple(sorted_input_list)

    return max_sum_tuple

def get_max_sum_tuple(sorted_input_list) -> tuple[int, int]:

    max_number_one = ""
    max_number_two = ""
    negative_index = None

    for index, number in enumerate(sorted_input_list):
        
        if number < 0:
            negative_index = index
            break

    if negative_index != None:

        for index, number in enumerate(sorted_input_list):
            
            if index == negative_index:
                break

            max_number_one += str(number)

        for i in range(negative_index, len(sorted_input_list)):

            if i == negative_index:
                max_number_two += str(sorted_input_list[i])
            else:
                max_number_two += str(sorted_input_list[i])[1:]
    else:
        for i in range(len(sorted_input_list)):

            if i % 2 == 0:
                max_number_one += str(sorted_input_list[i])
            else:
                max_number_two += str(sorted_input_list[i])
    
    return (int(max_number_one), int(max_number_two))

def mergesort(input_list: list) -> list:


    if len(input_list) <= 1:
        return input_list
    
    middle_index = len(input_list) // 2
    left_items = input_list[:middle_index]
    right_items = input_list[middle_index:]

    left_items = mergesort(left_items)
    right_items = mergesort(right_items)

    return merge(left_items, right_items)


def merge(left_items, right_items) -> list:

    merged_list = []

    left_index = 0
    left_items_size = len(left_items)
    right_index = 0
    right_items_size = len(right_items)

    while left_index < left_items_size and right_index < right_items_size:

        left_side_current_item = left_items[left_index]
        right_side_current_item = right_items[right_index]

        if left_side_current_item > right_side_current_item:

            merged_list.append(left_side_current_item)
            left_index += 1
        else:
            merged_list.append(right_side_current_item)
            right_index += 1

    potential_left_leftover = left_items[left_index:]
    potential_right_leftover = right_items[right_index:]

    merged_list += potential_left_leftover
    merged_list += potential_right_leftover

    return merged_list

def test_function(test_case: tuple[list[int], list[int]]) -> None:

    output: tuple[int, int] = rearrange_digits(test_case[0])
    solution: list[int] = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

if __name__ == '__main__':
    # Edge case: Single element list
    test_function(([9], [9, 0]))
    # Expected output: Pass

    # Normal case: Mixed positive and negative numbers
    test_function(([3, -2, 1, -4, 5], [531, -24]))
    # Expected output: Pass

    # Normal case: list with zeros
    test_function(([0, 0, 0, 0, 0], [0, 0]))
    # Expected output: Pass

    # Normal case: list with repeated numbers
    test_function(([2, 2, 2, 2, 2], [222, 22]))
    # Expected output: Pass

    test_function(([1, 2, 3, 4, 5], [542, 31]))
    test_function(([4, 6, 2, 5, 9, 8], [964, 852]))