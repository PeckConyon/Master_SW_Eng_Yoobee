class LocVal:
    
    def __init__(self, location:int):
        self.location = location
        self.value = ''
        self.player_id = ''
        #print(self.location)
        
    # Setters
    def set_value(self,value, player_id:str):
        self.value = value 
        self.player_id = player_id
        
    # Getters
    def get_location(self,location):
        return self.location

    def get_value(self,value):
        return self.value 
        