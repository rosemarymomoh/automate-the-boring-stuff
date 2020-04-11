def collatz(number):
    if number % 2 == 0: #if the provided number is even
        result = number // 2
        print(result)
        return result
    
    else: #if odd 
        result = 3 * number + 1 
        print(result)
        return result
        

print("Please enter in a number")
try: 
    num = int(input())
    while num != 1:
        num = collatz(num)

except ValueError:
    print('ValueError. This needs to be an integer')
   
    

