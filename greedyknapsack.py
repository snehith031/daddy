weights=list(map(int,input("enter weights:").split(",")))
price=list(map(int,input("enter price:").split(",")))
capacity=int(input("enter capacity:"))
f=[]
profit=0
for i in range(0,len(weights)):
    a=price[i]/weights[i]
    f.append(a)
for j in range(0,len(f)):
    k=f.index(max(f))
    if capacity>=weights[k]:
        profit=profit+price[k]
        capacity-=weights[k]
        f[k]=0
        weights[k]=0
    elif capacity!=0 and weights[k]>capacity:
        profit=profit+price[k]*(capacity/weights[k])
        print(profit)
        break

