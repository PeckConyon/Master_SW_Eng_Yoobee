from typing import List
from loc_val import LocVal

class Board:
    
    def __init__(self):
        self.board_values:List[LocVal] = []
        
        for i in range(9):
            self.board_values.append(LocVal(i+1))
        
    def set_loc_val(self, location:int , value: str, player_id : str):
        self.board_values[location].set_value(value, player_id)
        
    def check_pattern(self):
       
        for i in range(2):
            row_result = self.check_row(i + 1)
            if row_result != None:
                return row_result;
            
            col_result = self.check_col(i + 1)
            if col_result != None:
                return col_result;
            
        diag_result_1 = self.check_diagnol_1()
        if diag_result_1 != None:
            return diag_result_1;
        
        diag_result_2 = self.check_diagnol_2()
        if diag_result_2 != None:
            return diag_result_2;


    def check_row(self, row_no):
        obj_1 = self.board_values[row_no]
        obj_2 = self.board_values[row_no + 1]
        obj_1_3 = self.board_values[row_no + 2]        
        return self.is_match(obj_1,obj_2,obj_1_3)
    
    def check_col(self, col_no):
        obj_1 = self.board_values[col_no]
        obj_2 = self.board_values[col_no + 1]
        obj_3 = self.board_values[col_no + 2]        
        return self.is_match(obj_1,obj_2,obj_3)
    
    def check_diagnol_1(self):
        obj_1 = self.board_values[1]
        obj_2 = self.board_values[5]
        obj_3 = self.board_values[9]        
        return self.is_match(obj_1,obj_2,obj_3)
    
    def check_diagnol_2(self):
        obj_1 = self.board_values[3]
        obj_2 = self.board_values[5]
        obj_3 = self.board_values[7]        
        return self.is_match(obj_1,obj_2,obj_3)

    def is_match(self,obj_1_1,obj_1_2,obj_1_3):
        #if same player
        if(obj_1_1.player_id == obj_1_2.player_id == obj_1_3.player_id):
            if(obj_1_1.value == obj_1_2.value == obj_1_3.value):
                return obj_1_1.player_id  + " Wins"
        return None