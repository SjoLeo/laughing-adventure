rad_1 = [" "," "," "]
rad_2 = [" "," "," "]
rad_3 = [" "," "," "]
lista = [rad_1, rad_2, rad_3]

def image():
    print(f"""

     -----------
    | {lista[0][0]} | {lista[0][1]} | {lista[0][2]} |
    |-----------|
    | {lista[1][0]} | {lista[1][1]} | {lista[1][2]} |
    |-----------|
    | {lista[2][0]} | {lista[2][1]} | {lista[2][2]} |
     -----------

     """)

def player_1(kolumn, rad):
    lista[rad-1][kolumn-1] = "X"

def player_2(kolumn, rad):
    lista[rad-1][kolumn-1] = "O"  

image()
while True:
    
    while True:
        print("player 1")
        kolumn = int(input("kolumn: "))
        rad = int(input("rad: "))
        if lista[rad-1][kolumn-1] == " ":
            player_1(kolumn, rad)
            break
        else:
            print("")
            print("Ogiltigt")
            print("")
    image()

    print("player 2")

    while True:
        kolumn = int(input("kolumn: "))
        rad = int(input("rad: "))
        if lista[rad-1][kolumn-1] == " ":
                player_2(kolumn, rad)
                break
        else:
            print("")
            print("Ogiltigt")
            print("")
        
    image()


