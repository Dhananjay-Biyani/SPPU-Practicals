n = int(input("enter the number of items: "))
values = []
weights = []
for i in range(n):
    values.append(int(input(f"enter the value of item {i+1}: ")))
    weights.append(int(input(f"enter the weight of item {i+1}: ")))

capacity = int(input("enter the capacity of knapsack: "))


def knapsack(values , weights,capacity):
    n = len(values)
    dp = [[0]*(capacity+1) for i in range(n+1)] # creating table(2d matrix) to store the maximum value

    # itertaing through each item and possible capacity using recurrance relation
    for i in range(1,n+1):
        for w in range(capacity+1):
            if weights[i-1]<=w:
                dp[i][w] = max(dp[i-1][w], values[i-1]+dp[i-1][w- weights[i-1]])
            else:
                dp[i][w] = dp[i-1][w]

    max_value = dp[n][capacity]  # the maximum value is stored in the bottom right cell of the table 

    # trace back to find the selected values 
    selected_items = []
    i , j  = n , capacity
    while i >0 and j >0:
        if dp[i][j] != dp[i-1][j]:
            selected_items.append(i)
            j-= weights[i-1]
        i -= 1

    return max_value , selected_items

max_value, selected_items = knapsack(values, weights, capacity)

print("Maximum value:", max_value)
print("Selected items:", selected_items)