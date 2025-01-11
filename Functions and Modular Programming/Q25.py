def fibonacci():
    n=int(input("enter the number :"))
    if n<=0:
        return []
    if n==0:
        return [0]
    if n==2:
        return [0,1]
    else:
        fib=[0,1]
        for i in range(2,n):
            fib.append(fib[-1]+fib[-2])
            print(fib)
        return fib

fibonacci()
