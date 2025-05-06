import os
from ..File_Processors.image_processor import ImageProcessor
from ..File_Processors.data_file_processor import FileProcessor

class FileIdentifier:
    
    def __init__(self, file_path):
        self.file_path = file_path
        self.file_name_with_extension = os.path.basename(file_path) 
        self.file_name, self.extension  = os.path.splitext(self.file_name_with_extension)
        
    def __is_image(self):
        return self.extension.lower() in ['.jpg', '.jpeg', '.png', '.bmp']
    
    def __is_csv_parquet(self):
        return self.extension.lower() in ['.csv', '.parquet', '.txt']
    
    def start_process(self):
        if(self.__is_image()):
            image_processor =  ImageProcessor(self.file_path, self.extension)
            image_processor.process_image()
        elif(self.__is_csv_parquet()):
            file_processor = FileProcessor(self.file_path, self.extension)
            file_processor.process_file()
        else:
             print(f"File type {self.extension} not supported")
             return
         
        print(f"\nData loaded successfully from {self.file_path}")
        
            
    