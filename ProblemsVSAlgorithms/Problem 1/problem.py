def sqrt(number) -> int:

    if number == 0:
        return 0
    
    left = 0
    right = number
    
    while left <= right:
        middle = (left + right) // 2
        potential_square_root = middle * middle

        if potential_square_root == number:
            return middle
        
        if potential_square_root < number:
            left = middle + 1

        if potential_square_root > number:
            right = middle - 1

print("Pass" if 3 == sqrt(9) else "Fail")
print("Pass" if 0 == sqrt(0) else "Fail")
print("Pass" if 4 == sqrt(16) else "Fail")
print("Pass" if 1 == sqrt(1) else "Fail")
print("Pass" if 5 == sqrt(25) else "Fail")