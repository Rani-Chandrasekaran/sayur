'''
6. *Sum of Digits*
   - *Description*: Write a function that takes an integer and returns the sum of its digits.
   - *Input*: 123
   - *Output*: 6
   - *Input*: 987
   - *Output*: 24
'''
inputnum =(input("Enter the digits for SumOfDigits: "))
sum = 0
sum1 = 0
for i in inputnum:
    j= int(i)
    sum = int(sum + j)
print(f"The Sum Of Digits for {inputnum} is {sum}")

