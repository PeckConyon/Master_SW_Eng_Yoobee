from data_reader import DataReader

def main():
    data_reader = DataReader()

    print(f'***************** Basic Info ***************** \n')
    data_reader.get_info()
  
    print(f'\n***************** Sample Record ***************** \n {data_reader.get_sample_record()} \n')
    
    print(f'***************** Most Rained Month of 1950 ***************** \n {data_reader.get_most_rained_month_by_year(1950)} \n')
    
    print(f'***************** Average Rainfall of 1950 ***************** \n {data_reader.get_average_rainfall_by_year(1950)} \n')
    
    print(f'***************** Monthly Average Rainfall Chart ***************** \n')
    data_reader.show_chart_avg_monthly_rain()
 

if __name__ == "__main__":
    main()
