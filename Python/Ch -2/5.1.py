# Write a program to find the minimum number from the given three numbers using a nested statement.

'''

a=input("Enter your 1st number :")
b=input("Enter your 2nd number :")
c=input("Enter your 3rd number :")

if a<b:
    if a<c:
        print(a,"is minimum")
    else:
        print(c,"is minimum")

else:
    if b<c:
        print(b,"is minimum")
    else:
        print(c,"is minimum")


'''

'''
# Write a program to find the maximum number from the given four numbers using a nested statement.


a=input("Enter your 1st number")
b=input("Enter your 2nd number")
c=input("Enter your 3rd number")
d=input("Enter your 4th number")



if a>b:
    if a>c:
        if a>d:
            print(a,"is maximum")
        else:
            print(d,"is maximum")
    else:
        if c>d:
            print(c,"is maximum")
        else:
            print(d,"is maximum")
else:
    if b>c:
        if b>d:
            print(b,"is maximum")
        else:
            print(d,"is maximum")
    else:
        if c>d:
            print(c,"is maximum")
        else:
            print(d,"is maximum")


'''


# Input a number and print "Positive" if a number is larger than 0; otherwise print "Non-Positive" in a single line.

'''
num=float(input("Enter you number; "))

print(num,"is positive number" if num>=0 else "non-positive number")

'''


# Input marks and print "Pass" if marks ≥ 40; otherwise print "Fail" using shorthand if-else.

'''
marks=float(input("Enter Your Marks: "))
print(marks,"Congraulatons!! you are pass !" if marks>=40 else "You are fail, better luck next time ")




'''
# Input a number and print "Even" if even; otherwise print "Odd" using shorthand if-else.

'''
num=int(input("Enter Number"))
print(num,"is even number") if num%2==0 else ( print(num,"is odd number"))
'''

# Input a number and print "Even" if even; otherwise print "Odd" using shorthand if-else.

'''
num=int(input("Enter Number"))
print(num,"is even number") if num%2==0 else ( print(num,"is odd number"))