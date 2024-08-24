'''
8. *Check Prime Number*
   - *Description*: Write a function that checks if a given number is a prime number.
   - *Input*: 7
   - *Output*: True
   - *Input*: 8
   - *Output*: False
   '''
def primenumber(num):
    if num < 2 :
        return False
    if num == 2:
        return True
    if num > 2 and num % 2 == 0:
        return False
    if num % 3 != 0:
        return True

num = int(input("Enter the number to check the number is a prime number:" ))
if primenumber(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")