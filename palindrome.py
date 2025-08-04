x = input("Enter a string: ")

x = x.lower()

y = x[::-1]


if x == y:
    print(f"{x} is a palindrome")
else:
    print(f"{x} is not a palindrome")