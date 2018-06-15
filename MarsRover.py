posn = [0,0]


while True:
    print("Enter Distance to Continue Or write exit to exit")

    try:
        Distance = int(input("Enter Distance"))
    except ValueError:
        break
    else:
        print("Enter Direction"
              " North : 1"
              " South : 2"
              " East  : 3"
              " West  : 4")
        Direction = int(input())

        if (Direction == 1):
            posn[0] += Distance

        if (Direction == 2):
            posn[0] -= Distance

        if (Direction == 3):
            posn[1] += Distance

        if (Direction == 4):
            posn[1] -= Distance

        if (4 <= Direction <= 1):
            print("Direction Not Specified")

        print(posn)
