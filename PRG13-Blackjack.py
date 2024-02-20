import random

colors=("A","B","C","D")
values=("1","2","3","4","5","6","7","8","9","10","K","J","Q")

deck=[]

for color in colors:
    for value in values:
        deck.append(color+value)
        random.shuffle(deck)


print(deck)

print("---")

card=(deck[:2])
del deck[:2]
print(card)
