pn=10000

while True:
    ispn=True
    for p in range(2,pn):
        if pn%p==0:
            ispn=False
            break
    if ispn==True:
        print(pn)
    pn+=1
