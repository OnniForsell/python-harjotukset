luku = int(input("Anna tasaluku: "))
jako = 2

if luku > 1:
    for i in range(2, luku):
        if luku % jako == 0:
            print("Ei ole alkuluku")
            break
        jako += 1
    else:
        print("On alkuluku")