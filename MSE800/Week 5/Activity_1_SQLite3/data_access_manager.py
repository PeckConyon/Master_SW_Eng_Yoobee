import sqlite3
import os

class DataAccessManager:
    
    def __init__(self, db_name="car_rentals"):
        self.db_path = os.path.join(os.path.dirname(__file__), 'database', f"{db_name}.db")
        os.makedirs(os.path.dirname(self.db_path), exist_ok=True)
        self.db_connection = None
        self.cursor = None
    
    def _connect_database(self):  
        self.db_connection =  sqlite3.connect(self.db_path) 
        self.cursor = self.db_connection.cursor()
    
    def execute_query(self, sql, params: None):
        
        try:
        
            self._connect_database()
        
            if(params):
                self.cursor.execute(sql, params)
            else:
                self.cursor.execute(sql)
                
            self.db_connection.commit()
        except sqlite3.Error as e:
            print(f'Error {e}')
        finally:
            self._close_connection()
            
        
    def _close_connection(self):        
        self.cursor.close()
        self.db_connection.close()
        
    def fetch_data(self, sql):
        
        self._connect_database()
        rows = self.cursor.fetchall()
        
        
        