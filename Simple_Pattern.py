'''
*
**
***
****
*****
and so on.
'''

def simple_pattern(n):
    for i in range(1, n+1):
       print("*"*i) 

a=int(input("Enter any number: "))
simple_pattern(a)