n =(int(input("enter the number: ")))

def fibonacci(n):
    series = [0,1]
    steps =0
    if n<=0:
        print("n cannot be negative ")
    
    while len(series)<n:
        next = series[-1]+series[-2]
        series.append(next)
        steps+=1

    return series , steps

series , steps = fibonacci(n)
print("Fibonacci series is: ",series)
print("Total steps are: ",steps)