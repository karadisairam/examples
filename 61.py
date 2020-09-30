no=[10,20,0,5,0,30]
for n in no:
    if n==0:
        print("Hey howwe can divide with zero..just skipping :")
        continue
    print("100/{}={}".format(n,100/n))