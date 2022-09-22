"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Write a programn to find sum of first n even numbers.
"""
print("          PROGRAM STARTED            ")
print("_____________________________________")
print("Using While Loop")
n=int(input("How many even no. want to add:-"))
i=1
sum=0
count=0
while(count<n):
    if i%2==0:
        sum=sum+i
        count=count+1
    i=i+i
print("ans. ",sum)
print("_____________________________________")
print("Using For Loop.")
n=int(input("How many even no. want to add:-"))
i=1
sum=0
count=0
for count in range(1,n+1,1):
    if i%2==0:
        sum=sum+i
        count=count+1
    i=i+1
print("ans. ",sum)
print("_____________________________________")
print("          PROGRAM ENDED              ")