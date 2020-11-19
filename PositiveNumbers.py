#Write a Python program to print all positive numbers in a range

# creating an empty list
lst=[]

# number of elements as input
g=int(input("Enter numer of elements : "))

# iterating till the range
for i in range(0,g):
    ele=int(input())
    # adding the element
    lst.append(ele)

print("Input List ")
print(lst)

# List of positive numbers
lstp=[]

# Checking for positive numbers
for x in range(0,g):
    if lst[x]>0:
        # Appending positive numbers to lstp
        lstp.append(lst[x])

print("Output List ")
print(lstp)
        
