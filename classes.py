# class House:
#     address = ""
#     area = 0
#     rooms = 0
#     floors = 0

#     def get_info(self):
#         print(f"address is : {self.address} \narea: {self.area} \nrooms: {self.rooms} \nfloors: {self.floors}")


# first_house = House() # creating Object
# first_house.area = 200
# first_house.address = "123 first street"
# # print(first_house.adress)
# first_house.get_info()

# second_house = House()
# # print(second_house.area)


class Player:
    score= 0
    health = 100
    
    def __init__(self, username):
        self.username = username

    def __str__(self):
        return self.username

player1 = Player(username='test player')
print(player1)