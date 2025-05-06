import pandas as pd

class FileProcessor:
    
    def __init__(self, file_path, extension):
        self.file_path = file_path
        self.extension = extension
        self.file_data = None
        
    def process_file(self):
        try:
            if(self.extension == '.csv'):
                self.file_data = pd.read_csv(self.file_path)
            elif(self.extension == '.parquet'):
                self.file_data = pd.read_parquet(self.file_path)  
            else:
                print(f"Warning: Unsupported file format '{self.extension}'. Skipping processing file '{self.file_path}'")
                return
            
            print("\n******************************* Data Summary ***************************")
            print(self.file_data.info())
            print("\nMissing Values:")
            print(self.file_data.isnull().sum())
            print("\nDescriptive Statistics:")
            print(self.file_data.describe())
            
        except Exception as e:
            print(f"Error processing data file {self.file_path} : {e}")
            
        