def timer(time):

    day = int(time/86400)
    hour = int((time%86400)/3600)
    remaining = time % 86400
    minute = (remaining % 3600) // 60
    sec = time%60
    print(f"Your time is {day}d {hour}h {minute}m {sec}s")

time = int(input("Enter your time: "))

timer(time)