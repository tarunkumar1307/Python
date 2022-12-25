#write a program to take a number 'n' from the user and print even number 0 to nth number.
a=int(input("Enter any number: "))
for i in range(0, a+1):
    if i%2==0:
        print(i, end=" ")