#file name and what to import
from data_fileFormat_processor import DataProcessor
from circle_helper import CircleHelper

def main():
   
    file_path = 'sample_junk_mail.csv'  # or 'your_data_file.parquet'
    processor = DataProcessor(file_path)
    processor.load_data()
    processor.initial_processing();
    
    circle_helper = CircleHelper()
    value_to_cal_sin_cos = float(input('Enter a value to find sin and cos : ')) 
    sin = circle_helper.calculate_Sin(value_to_cal_sin_cos)
    print('sin of the value : ' + str(value_to_cal_sin_cos) + ' is ' + str(sin))
    
    cos = circle_helper.calculate_Cos(value_to_cal_sin_cos)
    print('cos of the value : ' + str(value_to_cal_sin_cos) + ' is ' + str(cos))
    
    diameter_of_cirlce = float(input('Enter the diameter of the circle to calculate area : '));
    area = circle_helper.calculate_circle_ara(diameter_of_cirlce)
    print('area of the cirlce with diameter : ' + str(diameter_of_cirlce) + ' is '+ str(area))
    

if __name__ == "__main__":
    main()
