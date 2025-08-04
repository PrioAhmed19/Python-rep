x = int(input("Enter a non negative number: "))

if x < 0 :
    print("Enter a non negative number")
elif x == 0:
    print(f"1 is the factorial output of {x}")
    
else:
    i = 1
    sum = 1
    while i in range(x+1):
        sum = sum*i
        i = i+1

    print(f"{sum} is the factorial output of {x}")
