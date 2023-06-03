
#Compute the sum of digits in all numbers from 1 to n.
#def sumn(n):
    #final_sum = 0
    #for x in range(n + 1):
        #final_sum = final_sum + x
        # final_sum += x
    #return final_sum

#test_data = 5 # 15
#test_result = sumn(test_data)
#print(test_result)

#Find the max number from 3 values
#def find_max(a, b, c):
   #if a > b and a> c:
        #return a
    #if b >a and b > c:
        #return b
    #return c

#test_result = find_max(15, 40, 20) #40
#print(test_result)

#count odd and even numbers
def count_odd_even(n):
    odds = 0
    evens = 0

    while n != 0:
        current_digit = n % 10
        if current_digit % 2:
            odds += 1
        else:
            evens += 1
            n = n // 10

    print(f"Evens: {evens}, Odds: {odds}"),


test_number = 14570 # Odds 1, 5, 7 Evens: 4, 0
count_odd_even(test_number)