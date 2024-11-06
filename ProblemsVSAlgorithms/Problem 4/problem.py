def sort_012(input_list):

    index_0 = 0
    index_2 = len(input_list) - 1
    front_index = 0

    while front_index <= index_2:
        
        if input_list[front_index] == 0:
            input_list[front_index] = input_list[index_0]
            input_list[index_0] = 0
            index_0 += 1
            front_index += 1
            continue

        if input_list[front_index] == 2:
            input_list[front_index] = input_list[index_2]
            input_list[index_2] = 2
            index_2 -= 1
            continue

        front_index += 1

    return input_list


def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")

test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])