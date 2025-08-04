while True:
    x = input("Enter a number: ")
    if x.isdigit():
        x = int(x)
        break
    else:
        print("Its not a valid integer")


x = str(x)

y = sorted(x)

print(y[-1])