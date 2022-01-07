def multilpy_3_5(limit):
    i=1
    sum=0
    while i<=limit:
        if i%3==0 or i%5==0:
            print("3 or 5 ke multipl",i)
            sum+=i
        i+=1
    print(sum)

a=int(input("enter the limit"))
multilpy_3_5(a)

    