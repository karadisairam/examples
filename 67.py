s=input("enter the str :")
i=0
for x in s:
    print("The cgar present at +ve index {} and at -ve index {}".format(i,i-len(s),x))
    i=i+1