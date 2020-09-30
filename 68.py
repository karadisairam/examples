s="welcome to python"
n=len(s)
i=0
print("forward direction")
while i<n:
    print(s[i],end='')
    i=i+1
print("back direction ")
i=-1
while i>=-n:
    print(s[i],end='')
    i=i-1
    