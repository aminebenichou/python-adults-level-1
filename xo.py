indexes = [
    ["1", "2", "3"],
    ["4", "5", "6"],
    ["7", "8", "9"]
]
def table():
    i=0
    while i<2:
        print(f" {indexes[i][0]}  |  {indexes[i][1]} |  {indexes[i][2]} ")
        print("____|____|____")
        i += 1
    print(f" {indexes[2][0]}  |  {indexes[2][1]} | {indexes[2][2]}  ")
    print("    |    |    ")

def changeValues(player_input, player):
    i = 0
    while i<len(indexes):
        j=0
        while j<len(indexes[i]):
            if player_input == indexes[i][j]:
                indexes[i][j] = player
                break
            j += 1
        i += 1




turn = 1
running = True
is_null= False
winner=False
digits =[]
while running:
    player = 'x'
    if turn%2 == 0:
        player = 'o'
    
    table()
    print('turn number: ', turn)
    player_input = input("Enter a valid number : ")
    changeValues(player_input, player)
    turn += 1


    y=0
    
    while y<len(indexes):
        if (indexes[y][0] == indexes[y][1] == indexes[y][2]) or (
            indexes[0][y] == indexes[1][y] == indexes[2][y]) or (
            indexes[y][y] == indexes[1][1] == indexes[2][2]) or (
            indexes[0][-1] == indexes[1][1] == indexes[2][0]):

            table()
            winner= True
            running = False

        if turn>9:
            for element in indexes[y]:
                try:
                    number = int(element)
                    digits.append(number)
                except:
                    print(f'')

            if digits == []:
                
                running=False

        y += 1

    if winner:
        print(f'congrats {player}')