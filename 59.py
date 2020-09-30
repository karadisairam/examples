#To print evne numbers

n = int(input("enter the number :"))
for i in range(n):
    if i%2!=0:
        continue
    print(i)