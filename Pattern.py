'''
    *
   **
  ***
 ****
*****
'''

def pattern(n):
    i=1
    while i<=n:
        print(" "*(n-i), end="")
        print("*"*i)
        i+=1

a=int(input("Enter any Number(0-9): "))
pattern(a)