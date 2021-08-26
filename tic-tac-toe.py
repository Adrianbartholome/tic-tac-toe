import random

x = 'x'
o = 'o'
turn = True
a = b = c = d = e = f = g = h = i = '¿'
varList = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i')
ans = ""


def win():
    print('You win!')
    quit()


def lose():
    print('You lose!')
    quit()


def tie():
    print("Its a tie!")
    quit()


def checkWin():
    if ((a == b == c) or (a == d == g) or (a == e == i)) and (a != '¿'):
        if (a == 'x'):
            win()
        else:
            lose()
    elif ((d == e == f) or (b == e == h) or (c == e == g)) and (e != '¿'):
        if (e == 'x'):
            win()
        else:
            lose()
    elif ((g == h == i) or (c == f == i)) and (i != '¿'):
        if (i == 'x'):
            win()
        else:
            lose()
    elif all(i != '¿' for i in (a, b, c, d, e, f, g, h, i)):
        tie()


def pBoard():
    print(f"""
         |   |   
       {a} | {b} | {c}
      ___|___|___
         |   |   
       {d} | {e} | {f}
      ___|___|___
         |   |   
       {g} | {h} | {i}
         |   |
    """)


welcome = """
Tic-tac-toe!

Press 'q' to quit.\n
1 2 3
4 5 6
7 8 9
"""
print(welcome)

while (ans != 'q'):
    if (ans == '1'):
        if (a == x) or (a == o):
            print('Choose a different position')
        else:
            a = x
            turn = True
    elif (ans == '2'):
        if (b == x) or (b == o):
            print('Choose a different position')
        else:
            b = x
            turn = True
    elif (ans == '3'):
        if (c == x) or (c == o):
            print('Choose a different position')
        else:
            c = x
            turn = True
    elif (ans == '4'):
        if (d == x) or (d == o):
            print('Choose a different position')
        else:
            d = x
            turn = True
    elif (ans == '5'):
        if (e == x) or (e == o):
            print('Choose a different position')
        else:
            e = x
            turn = True
    elif (ans == '6'):
        if (f == x) or (f == o):
            print('Choose a different position')
        else:
            f = x
            turn = True
    elif (ans == '7'):
        if (g == x) or (g == o):
            print('Choose a different position')
        else:
            g = x
            turn = True
    elif (ans == '8'):
        if (h == x) or (h == o):
            print('Choose a different position')
        else:
            h = x
            turn = True
    elif (ans == '9'):
        if (i == x) or (i == o):
            print('Choose a different position')
        else:
            i = x
            turn = True
    else:
        print('Choose a position, 1-9\n')

    pBoard()
    checkWin()

    if turn:
        while True:
            if (((2 * x in (a + b + c)) and ('¿' in (a + b + c))) or (2 * o in (a + b + c)) and ('¿' in (a + b + c))):
                z = ('a', 'b', 'c')
                for zz in z:
                    if (locals()[zz] == '¿'):
                        locals()[zz] = o
                        break
                turn = False
                break
            elif (((2 * x in (d + e + f) and ('¿' in (d + e + f))) or (2 * o in (d + e + f))) and ('¿' in (d + e + f))):
                z = ('d', 'e', 'f')
                for zz in z:
                    if (locals()[zz] == '¿'):
                        locals()[zz] = o
                        break
                turn = False
                break
            elif (((2 * x in (g + h + i) and ('¿' in (g + h + i))) or (2 * o in (g + h + i))) and ('¿' in (g + h + i))):
                z = ('g', 'h', 'i')
                for zz in z:
                    if (locals()[zz] == '¿'):
                        locals()[zz] = o
                        break
                turn = False
                break
            elif (((2 * x in (a + d + g) and ('¿' in (a + d + g))) or (2 * o in (a + d + g))) and ('¿' in (a + d + g))):
                z = ('a', 'd', 'g')
                for zz in z:
                    if (locals()[zz] == '¿'):
                        locals()[zz] = o
                        break
                turn = False
                break
            elif (((2 * x in (b + e + h) and ('¿' in (b + e + h))) or (2 * o in (b + e + h))) and ('¿' in (b + e + h))):
                z = ('b', 'e', 'h')
                for zz in z:
                    if (locals()[zz] == '¿'):
                        locals()[zz] = o
                        break
                turn = False
                break
            elif (((2 * x in (c + f + i) and ('¿' in (c + f + i))) or (2 * o in (c + f + i))) and ('¿' in (c + f + i))):
                z = ('c', 'f', 'i')
                for zz in z:
                    if (locals()[zz] == '¿'):
                        locals()[zz] = o
                        break
                turn = False
                break
            elif (((2 * x in (a + e + i) and ('¿' in (a + e + i))) or (2 * o in (a + e + i))) and ('¿' in (a + e + i))):
                z = ('a', 'e', 'i')
                for zz in z:
                    if (locals()[zz] == '¿'):
                        locals()[zz] = o
                        break
                turn = False
                break
            elif (((2 * x in (g + e + c) and ('¿' in (g + e + c))) or (2 * o in (g + e + c))) and ('¿' in (g + e + c))):
                z = ('g', 'e', 'c')
                for zz in z:
                    if (locals()[zz] == '¿'):
                        locals()[zz] = o
                        break
                turn = False
                break
            else:
                opp = str(random.choice(varList))
                if (locals()[opp] == '¿'):
                    locals()[opp] = o
                    turn = False
                    break
    print("AI: ")
    pBoard()
    checkWin()

    ans = input("Your move: ")