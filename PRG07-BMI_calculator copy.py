height=1.8
weight=90

height*=height
x=weight/height

if x<18.4:
    print("Velká podváha")
else:
    if x<19.9:
        print("Podváha")
    else:
        if x<24.9:
            print("Normalní")
        else:
            if x<29.9:
                print("Nadváha")
            else:
                if x<34.9:
                    print("Obezita 1. stupně")
                else:
                    if x<39.9:
                        print("Obezita 2. stupně")
                    else:
                        if x>40:
                            print("Obezita 3. stupně")

print (x)
                