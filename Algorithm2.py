#Given a string. Split it into two equal parts.
#Swap these parts and return the result.
#If the string has odd characters,
# #the first part should be one character greater than the second part.

def split_and_swap(s):
    length = len(s)
    half_length = length // 2

    # Swap these parts and return the result.
    first_part = s[:half_length +1:]
    second_part = s[half_length +1:]

    # If the string has odd characters
    if first_part != 0:
        first_part = s[:half_length +1:]
        second_part = s[half_length + 1:]

        return second_part + first_part

s = "bbbbbcaaaaa"
result = split_and_swap(s)
print(result)












