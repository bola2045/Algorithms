#When given a list
#the program should return a list of all the elements
# below the original list’s arithmetical mean.
# The arithmetical mean is the sum of all elements divided by the number of elements.


#def return_the_list_of_all_element(s):
    #length = len(s)
    #return length


#def sum_of_list(numbers):
   # total = 0
    #for number in numbers:
          #total += number
    #return total


#def elements_below_mean(s):
    #mean = sum_of_list(s) / len(s)
    #below_mean = mean, +str(mean)
    #return below_mean

#test_data = [1, 3, 5, 6, 4, 10, 2, 3] # 4.25
#print(return_the_list_of_all_element(test_data))


#When given a list of elements,
#find the two lowest elements.
#They can be equal to each other or different.

def find_min(arr):
    min = current_num = arr[0]
    for num in arr[1:]:
        current_num = min(current_num + num, num)
        min = min(current_num, min)

