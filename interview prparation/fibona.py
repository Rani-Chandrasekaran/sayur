'''
3. *Fibonacci Sequence*
   - *Description*: Write a function that returns the nth number in the Fibonacci sequence.
   - *Input*: 5
   - *Output*: 5
   - *Input*: 7
   - *Output*: 13
'''
def fibonacciseq(num):
   
   f1 = 0
   f2 = 1
   fibseq = []
   print(f"Fibonacci series for {num }: ")
   for i in range(0,num+1): 
      fibseq.append(f1)
      f3 = f1 + f2
      f1 = f2
      f2 = f3
   return fibseq

num =int(input("Enter your fibonacci number:"))
seq = fibonacciseq(num)
n = int(input("Enter the position to display in sequence:"))
print(seq[n])

     