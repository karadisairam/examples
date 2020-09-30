s=input("enter the string :")
i=0
for  x in s:
    print("The char present at positive index {} ans at negative index {} is {}".format(i,i-len(s),x))
    i=i+1