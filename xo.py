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

def changeValues(player_input):
    i = 0
    while i<len(indexes):
        j=0
        while j<len(indexes[i]):
            if player_input == indexes[i][j]:
                indexes[i][j] = "x"
                break
            j += 1
        i += 1





while True:
    table()
    player_input = input("Enter a valid number : ")
    changeValues(player_input)
