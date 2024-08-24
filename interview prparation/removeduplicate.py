'''
10. *Remove Duplicates*
    - *Description*: Write a function that takes a list and returns a new list with all duplicates removed.
    - *Input*: [1, 2, 2, 3, 4, 4, 5]
    - *Output*: [1, 2, 3, 4, 5]
    - *Input*: ['apple', 'banana', 'apple', 'orange']
    - *Output*: ['apple', 'banana', 'orange']
    '''
def removeduplicate(list):
    uniquelist = []
    for element in list:
        if element not in uniquelist:
            uniquelist.append(element)
    return uniquelist
input1 = [1, 2, 2, 3, 4, 4, 5]
print(removeduplicate(input1))

input2 = ['apple', 'banana', 'apple', 'orange']
print(removeduplicate(input2))