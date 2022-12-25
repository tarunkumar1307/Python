#Pattern
'''
      *
    * * *
   * * * *
  * * * * *
 * * * * * *
* * * * * * *
'''
def pyramid(n):
    k=1
    i=1
    while i<=n:
        b=1
        while b<=n-i:
            print(" ", end='')
            b=b+1
        j=1
        while j<=k:
            print('*', end='')
            j=j+1
        k=k+2
        print()
        i=i+1
n=int(input("Enter any number:"))
pyramid(n)
