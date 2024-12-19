class xo:
    indexes = [
        ["1", "2", "3"],
        ["4", "5", "6"],
        ["7", "8", "9"]
    ]
    turn = 1
    running = True
    is_null= False
    winner=False
    digits =[]


    def draw_table(self):
        i=0
        while i<2:
            print(f" {self.indexes[i][0]}  |  {self.indexes[i][1]} |  {self.indexes[i][2]} ")
            print("____|____|____")
            i += 1
        print(f" {self.indexes[2][0]}  |  {self.indexes[2][1]} | {self.indexes[2][2]}  ")
        print("    |    |    ")


    def changeValues(self, player_input, player): # change values of selected cell in the table
        i = 0
        while i<len(self.indexes):
            j=0
            while j<len(self.indexes[i]):
                if player_input == self.indexes[i][j]:
                    self.indexes[i][j] = player
                    break
                j += 1
            i += 1

    def play(self):
        while self.running:
            player = 'x'
            if self.turn%2 == 0:
                player = 'o'
            
            self.draw_table()
            print('turn number: ', self.turn)
            player_input = input("Enter a valid number : ")
            self.changeValues(player_input, player)
            self.turn += 1
            is_winner = self.check_winner()
            if is_winner:
                print(f'congrats {player}')

    def check_winner(self):
        y=0
        # chekc for winner in all positions
        while y<len(self.indexes):
            if (self.indexes[y][0] == self.indexes[y][1] == self.indexes[y][2]) or (
                self.indexes[0][y] == self.indexes[1][y] == self.indexes[2][y]) or (
                self.indexes[y][y] == self.indexes[1][1] == self.indexes[2][2]) or (
                self.indexes[0][-1] == self.indexes[1][1] == self.indexes[2][0]):

                self.draw_table()
                self.winner= True
                self.running = False
                
                return True
                
            # check if the result is null
            if self.turn>9:
                for element in self.indexes[y]:
                    try:
                        number = int(element)
                        self.digits.append(number)
                    except:
                        print(f'')

                if self.digits == []:
                    
                    self.running=False

            y += 1


game = xo()
game.play()