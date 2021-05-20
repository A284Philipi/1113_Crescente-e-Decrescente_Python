cont = int(0)
while cont == 0:
    a, b = input().split(" ")
    a = int(a)
    b = int(b)
    if a == b:
        cont = 1
    else:
        if a > b:
            print("Decrescente")
        else:
            print("Crescente")