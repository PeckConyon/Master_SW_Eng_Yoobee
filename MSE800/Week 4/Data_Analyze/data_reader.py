import os
import pandas as pd


class DataReader:
    
    def __init__(self):
        
        self.base_dir = os.path.dirname(os.path.abspath(__file__))  # Path to Advanced__File_Handler
        self.data_source = os.path.join(self.base_dir, 'Files','1924-to-1987_monthly-anually_rainfall.csv')
        self.data_frame = pd.read_csv(self.data_source) 
        
    def get_info(self):
        return self.data_frame.info()
    
    def get_sample_record(self):
        return self.data_frame.head(1)
     
    def get_most_rained_month_by_year(self, year):
        year_filter = self.data_frame["YEAR"] == year
        
        year_row = self.data_frame[year_filter]        
        
        #***************** Sample Record *****************
        #YEAR  JANUARY  FEBRUARY  MARCH  APRIL    MAY   JUNE  JULY  AUGUST  SEPTEMBER  OCTOBER  NOVEMBER  DECEMBER  ANNUAL
        #1924    105.7      92.9   91.2  307.2  334.4  191.8  90.9   100.4      127.9    180.1      77.2     186.3  1886.0
        
        monthly_data = year_row.drop(columns=["YEAR", "ANNUAL"]).iloc[0]  #.iloc[0] DF to series 
        
        most_rained_month = monthly_data.idxmax()
        
        return most_rained_month
    
    def get_average_rainfall_by_year(self, year):
        year_filter = self.data_frame["YEAR"] == year
        
        year_row = self.data_frame[year_filter]        
        
        #***************** Sample Record *****************
        #YEAR  JANUARY  FEBRUARY  MARCH  APRIL    MAY   JUNE  JULY  AUGUST  SEPTEMBER  OCTOBER  NOVEMBER  DECEMBER  ANNUAL
        #1924    105.7      92.9   91.2  307.2  334.4  191.8  90.9   100.4      127.9    180.1      77.2     186.3  1886.0
        
        monthly_data = year_row.drop(columns=["YEAR", "ANNUAL"]).iloc[0]  #.iloc[0] DF to series 
        
        average_rain_fall = monthly_data.mean()
        
        return average_rain_fall
   