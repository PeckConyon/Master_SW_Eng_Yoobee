import pandas as pd
from flower import Flower

class DataReader:
    
    def __init__(self):
        self.data_source = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
        self.flowers = []
        
    def read_iris_data(self):
        # https://pandas.pydata.org/pandas-docs/stable/user_guide/io.html#io-chunking
        data_frame = pd.read_csv(self.data_source,header=None, chunksize=1) # with chunk size can read row by row and iteratable (TextFileReader)
        for chunk in data_frame:
            row = chunk.iloc[0]
          # Skip empty lines 
            if row.isnull().any():
                continue
            flower = Flower(
                sepal_length=row[0],
                sepal_width=row[1],
                petal_length=row[2],
                petal_width=row[3],
                name=row[4]
            )
            self.flowers.append(flower)
            
    def get_unique_flower_names(self):
        unique_names = set() # set automatically ignores duplicates
        for flower in self.flowers:
            unique_names.add(flower.name)
        return unique_names
        