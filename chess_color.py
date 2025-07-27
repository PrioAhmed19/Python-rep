def chess_color(col,row):
    if col%2 ==  row%2:
        return "White"
    else:
        return "black"

col = int(input("Entry the column num: "))
row = int(input("Entry the row num: "))

print(chess_color(col,row))