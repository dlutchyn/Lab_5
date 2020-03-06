class Building:
    def __init__(self, address):
        self.address = address
    
    def __str__(self):
        return f"This building's address is {self.address}."


class House(Building):
    def __init__(self, address, room_list):
        super().__init__(address)
        self.room_list = room_list
    
    def __str__(self):
        return f"This house is at address {self.address} and has\
rooms: {self.room_list}."