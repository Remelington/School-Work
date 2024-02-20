import random


w, h, mines = 5, 5,3 

field = []


if mines> w*h:
    mines=0
    print ("Error: Too many mines.")

for x in range(w):
    row = []
    for y in range(h):
        row.append(0)
    field.append(row)

for i in range(mines):
    while True:
        rx = random.randint(0, w - 1)
        ry = random.randint(0, h - 1)
        if field[rx][ry] != "M":
            field[rx][ry] = "M"
            #print("mina na pozici:","x =",rx,".","y =",ry)
            break

deltas = ((-1,-1),())
for y in range(h):
    for x in range(w):    
        if field[x][y] == "M":
            for delta in deltas:
                nx=x+delta[0]
                ny=y+delta[1]
                if nx>=   
        print(field[x][y], end="")
    print()