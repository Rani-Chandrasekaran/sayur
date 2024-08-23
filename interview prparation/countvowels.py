'''
5. *Count Vowels*
   - *Description*: Write a function that counts the number of vowels in a given string.
   - *Input*: "hello world"
   - *Output*: 3
   - *Input*: "Python"
   - *Output*: 1
'''
vowels ='aeiou'
inputword1 = "hello word"
inputword2 = "Python"
inputword1count = 0
inputword2count = 0
for ch in inputword1:
    if ch in vowels:
        inputword1count = inputword1count +1
print(f"Number of vowels in the word {inputword1} is {inputword1count}")
for ch in inputword2:
    if ch in vowels:
        inputword2count = inputword2count +1
print(f"Number of vowels in the word {inputword2} is {inputword2count}")

