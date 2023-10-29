n = int(input("enter the number of values and weights:- "))
values = []
weights = []

capacity = int(input("enter the capacity of the knapsack:-"))
for i in range(n):
    v = int(input("enter the value:- "))
    values.append(v)
    w = int(input("enter the weight:- "))
    weights.append(w)


def knapsack(values,weights,capacity):
    n = len(values)
    ratio = [(values[i]/weights[i],i)for i in range(n)]
    ratio.sort(reverse=True)

    total = 0
    for i in range(n):
        index = ratio[i][1]
        if weights[index]<=capacity:
            total+=values[index]
            capacity-=weights[index]
        else:
            total+=(capacity/weights[index])*values[index]
            break

    return total 

result = knapsack(values,weights,capacity)
print("maximum value in knapsack is: ",result)