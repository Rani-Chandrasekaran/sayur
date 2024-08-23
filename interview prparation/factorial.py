'''
7. *Find Factorial*
   - *Description*: Write a function that computes the factorial of a given number.
   - *Input*: 4
   - *Output*: 24
   - *Input*: 5
   - *Output*: 120
   '''
def factorialnum(num):
    fact = 1
    factval = 0 
    for i in range(1,num+1):
        factval = i * fact
        fact = factval

    return factval

num = int(input("EnterFactorial: "))
print(f"The factorial for the number {num} is:")
print(factorialnum(num))



