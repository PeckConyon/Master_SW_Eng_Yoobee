from data_reader import DataReader

def main():
    data_reader = DataReader()
    data_reader.read_iris_data()
    unique_flower_names = data_reader.get_unique_flower_names()
    
    print('Flower names in IRIS dataset : \n')
    for flower_name in unique_flower_names:
        print(f'\t {flower_name}')   
    

if __name__ == "__main__":
    main()
