import random
colors={"R":"RED","G":"GREEN","B":"BLUE", "M": "MAGENTA"}
secret=[]
cnt_filed=3

color_codes=[]
for code in colors:
    color_codes.append(code)
rnd=random.randint(0, len(colors)-1)
code=color_codes[rnd]
color=colors[code]

print(rnd, code, color)