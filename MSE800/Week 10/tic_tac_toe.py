from board import Board

def main():
    
    print("TIC TAC TOE")
    board = Board()
    
    player_1 = input("Enter Name of the player : ")
    player_2 = "PC"
    current_player = player_1
    
    for i in range(8):
        print("Current Player : " + current_player)
        location = get_location()
        value = get_value()
        board.set_loc_val(location,value,current_player)
        if(i%2 == 0):
            current_player = player_2
        else:
            current_player = player_1
        
        result = board.check_pattern()
        print(result)
            
      
        

# Function to get the location of the board
def get_location():
    loc = input("Enter location (1,2,3,4,5,6,7,8,9) :")
    try:
        loc_index = int(loc)
        if(loc_index <1 or loc_index >10):
            print("Invalid location. Shoud be 1-9")
    except:
        print("Invalid location")
    #print(loc)
    return loc_index
    
# Function to read the value
def get_value():
    value = input("Enter value (X,O) :")
    try:
        if(value.lower() != 'x' and value.lower() != 'o'):
            print("Invalid value. Shoud be X or O")
    except:
        print("Invalid value")
    #print(value)
    return value
    
     
     
     
     
     
if __name__ == "__main__":
    main()