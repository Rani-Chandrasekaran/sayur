'''

9. *Merge Two Lists*
   - *Description*: Write a function that merges two lists into a single list.
   - *Input*: ([1, 2, 3], [4, 5, 6])
   - *Output*: [1, 2, 3, 4, 5, 6]
   - *Input*: (['a', 'b'], ['c', 'd'])
   - *Output*: ['a', 'b', 'c', 'd']
   '''
def mergetwolist(l1,l2):
    l1.extend(l2)
    return l1

l1 = [1, 2, 3]
l2 = [4, 5, 6]
print("Merged List:",mergetwolist(l1,l2))


l1 = ['a', 'b']
l2 = ['c', 'd']
print("Merged List:",mergetwolist(l1,l2))
    