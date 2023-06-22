#Your input is a list of integers,
#you have to reorder its entries so that the even entries appear first
#You are required to solve it without allocating additional storage
#operate with the input list).

# def input_is_a_list_of_integers(sort):
#     array = [7, 3, 5, 6, 4, 10, 3, 2]
#     sort(array)
#     return array


# def reorder_entries(first):
#     odd = 0
#     even = len(first) - 1
#
#     while odd < even:
#         # Look for odd number until found
#         while first[odd] // 2 == 0 and odd < even:
#             odd += 1

        # Look for even number until found
#             while first[even] // 2 != 0 and odd < even:
#                 even -= 1
#
#     return even
#
#
# test_data = ['7, 3, 5, 6, 4, 10, 3, 2']  # first(even) = 6,4,10,2  : # odd = 7,3,5,3
# print(reorder_entries(test_data))


# Write a program that takes as input
# a list of digits encoding a nonnegative decimal integer D
# and updates the list to represent the integer D + 1.


def increment_number(digits):
    digits = 0
    d = len(digits)
    power = digits + 1

    for i in range(digits -1, -1, -1):
        digits[i] += power

        if digits[i] < 10:
            power = 0

    digits[i] = 0

    if power == 1:
        digits.insert(0,1)

        return digits


test_data = [1, 2, 9]   # updated_data  [1, 3, 0]
print(test_data)
























