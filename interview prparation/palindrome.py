'''
2. *Check for Palindrome*
   - *Description*: Write a function that checks if a given string is a palindrome (reads the same forward and backward).
   - *Input*: "racecar"
   - *Output*: True
   - *Input*: "hello"
   - *Output*: False
   '''
InputWord = input("Enter pallindrome Word :")
rev_InputWord = ""
for ch in InputWord:
    rev_InputWord = ch + rev_InputWord
#print(rev_InputWord)
if InputWord .upper() == rev_InputWord.upper():
    print(f"{InputWord} is a Pallindrome Word ")
else:
     print(f"{InputWord} is  not a Pallindrome Word ")
