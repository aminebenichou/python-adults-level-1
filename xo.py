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
while True:
    player = 'x'
    if turn%2 == 0:
        player = 'o'
    
    table()
    print('turn number: ', turn)
    player_input = input("Enter a valid number : ")
    changeValues(player_input, player)
    turn += 1

# indexes[0][0] == indexes[0][1] == indexes[0][2]
# indexes[1][0] == indexes[1][1] == indexes[1][2]
# indexes[2][0] == indexes[2][1] == indexes[2][2]
