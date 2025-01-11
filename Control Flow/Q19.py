num=int(input("enter the number for sum of even and odd"))
even,odd=0,0
for i in range(num+1):
    if i%2==0:
        even+=i
    else:
        odd+=i
print(f"the sum of even numbers is {even} and the odd is {odd}")