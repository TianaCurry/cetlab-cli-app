#!/usr/bin/env python3

# libraries
import pandas as pd
import numpy as np
import os
from datetime import date , timedelta

class ReDataframes:
    def __init__(self, imported, exported=None, year=None):
        self.imported = imported
        self.exported = exported
        self.year = year

    # creating a user-defined function UDF for lesotho electricity demand data set 
    def clean_LS(self):
      # for Lesotho data
      """ This function will clean raw data sets in the format of the Lesotho_Load_Profile_2017_2019 xlsx file
          and create a dataframe with the demand,hour,year,month,day columns from the dataset. Then it will export a csv file to your directory. 
          - The arugment 'self.imported' is the path to where you stored your xlsx file with the data set to clean 
          - The argument 'self.exported' is the path to where you want to store the new 'clean' csv file dataframe: 
                      example - '/(your desired directory path)/(name of file).csv'""" 
      path = self.imported 
      lesotho_raw_data_df = pd.read_excel(path, sheet_name = "2018")                 # pulling the second sheet from the xlsx file and automatically turns the results into a dataframe 

      #pulling desired columns using iloc and drop funciton
      lesotho_df = lesotho_raw_data_df.iloc[:, 1:4].drop([0,1],axis= 0).copy()       # using iloc() to pull desired columns into a dataframe and using drop() to drop the first two rows 
      lesotho_df.rename(columns={'Unnamed: 1':"date_time","Unnamed: 2":"hour", "Unnamed: 3":"system_demand_[mw]"}, inplace = True) # renaming columns with inplace = True
      
      LESO_df = lesotho_df.reset_index(drop = True)                                  # reseting index 
      LESO_df['date_time'] = LESO_df['date_time'].astype('str')                      # changing date_time data type into string 

      LESO_df[['date','time']] = LESO_df.date_time.str.split(" ", expand=True)       # spliting the date_time column into 2 new columns titled date and hour
      LESO_df[['year','month','day']] = LESO_df.date.str.split("-", expand=True)     # spliting the date column into 3 new columns titled year month day
      lesotho_demand_df = LESO_df.iloc[:, 1:8].copy()                                # creating new dataframe not including first column at 0
      lesotho_demand_df.drop(["date","time"], axis=1, inplace = True)                # droping columns titled data and time 
      
      lesotho_demand_df['hour'] = lesotho_demand_df['hour'].astype('str')            # converting to string to convert to datetime value 
      lesotho_demand_df['hour'] = pd.to_datetime(lesotho_demand_df['hour'])          # converting hour column from string value to datetime value 
      lesotho_demand_df['hour'] = lesotho_demand_df['hour'].dt.hour                  # pulling only hour value from datetime value as a float value
      
      lesotho_demand_df['hour'] = lesotho_demand_df['hour']+1                        # converting hour from counting 0-23 to 1-24 
      
      lesotho_demand_df['system_demand_[mw]'] = lesotho_demand_df['system_demand_[mw]']/1000  # converting raw data from KW to MW by dividing by 1000
      lesotho_demand_df = lesotho_demand_df[['hour','day','month','year','system_demand_[mw]']].astype('int')
      
      lesotho_demand_df.to_csv(self.exported , index=False)                                      # exporting a csv file into given directory
      return

    #creating a User-defined function UDF of the above code 
    def clean_NA(self):
        # for Namibia data
        """ This function will clean raw data sets in the format of the NA_Hourly_Load_Generation_Imports_2018 xlsx file
            and create a dataframe with the demand,hour,year,month,day columns from the dataset. Then it will export a csv file to your directory. 
            - The arugment 'self.imported' is the path to where you stored your xlsx file with the data set to clean 
            - The argument 'self.exported' is the path to where you want to store the new 'clean' csv file dataframe: 
                        example - '/(your desired directory path)/(name of file).csv' """  
        path = self.imported                                            # give location of file you want to read inbetween ''
        namibia_df = pd.read_excel(path)                    # reads xlsx file using pandas and states first columm including index 
        
        namibia_demand_df = namibia_df.iloc[:, 0:2].copy()  # create a data frame using the first 3 columns including index 
        
        # change the column names in the data frame w/ inplace = True
        namibia_demand_df.rename(columns={"Date Time":"date_time", "System Demand [MW]":"system_demand_[mw]"}, inplace = True)
        namibia_demand_df['date_time'] = namibia_demand_df['date_time'].astype('str')                  # changing date_time data type into string 
        
        namibia_demand_df[['date','hour']] = namibia_demand_df.date_time.str.split(" ", expand=True)   # spliting the date_time column into 2 new columns titled date and hour   
        namibia_demand_df[['year','month','day']] = namibia_demand_df.date.str.split("-", expand=True) # splitint the date column into 3 new columns titled year month day 
        
        NA_demand_df = namibia_demand_df.iloc[:, 1:7].copy()                # creating new dataframe not including first column at 0  
        NA_demand_df.drop(columns= "date", inplace = True , axis = 1)       # droping column titled "date" from dataframe
        
        NA_demand_df['hour'] = pd.to_datetime(NA_demand_df['hour'])         # converting hour column from string into datetime values
        NA_demand_df['hour'] = NA_demand_df['hour'].dt.hour                 # converting hour columning to only show hour value as float value
        NA_demand_df['hour'] = NA_demand_df['hour']+1                       # changing hour from 0-23 to 1-24 
        
        NA_demand_df = NA_demand_df.drop(NA_demand_df.index[8760])          # Dropping last row in dataframe because not a part of timeseries
        NA_demand_df = NA_demand_df.round(0).astype(int)                    # converting dataframe into int values by rounding values first
        NA_demand_df.to_csv(self.exported, index=False)                                # exporting a csv file into given directory
        return
    
    # creating a User-defined function UDF for Republic of South Africa electricity demand data set 
    def clean_ZA(self):
        # for South Africa data
        """ This function will clean raw data sets in the format of the Eskom_RSA_Load_RE_Jan_2016_Jun_2019 xlsx file
            and create a dataframe with the demand,hour,year,month,day columns from the dataset. Then it will export a csv file to your directory. 
            - The arugment 'self.imported' is the path to where you stored your xlsx file with the data set to clean 
            - The argument 'self.exported' is the path to where you want to store the new 'clean' csv file dataframe: 
                        example - '/(your desired directory path)/(name of file).csv' """  
        path = self.imported                                                               # give location of file you want to read inbetween ''
        SA_sheets_data = pd.read_excel(path, sheet_name = ['RE_Hourly_kWh','System_Hourly_MWh']) # loads both sheets of the xlsx raw data set as a OrderedDict 
        south_africa_df = pd.read_excel(path, sheet_name = 1)                  # putting the second sheet from the xlsx file and automatically turns the results into a dataframe  
        SA_demand_df = south_africa_df.iloc[:, 0:3].copy()                     # create a data frame using the first 3 columns including index

        # change the column names in the data frame w/ inplace = True
        SA_demand_df.rename(columns={"SETTLEMENT_DATE":"date", "PERIOD":"hour", "SYSTEMENERGY": "system_demand_[mw]"}, inplace = True) 
        
        SA_demand_df['date'] = SA_demand_df['date'].astype('str')              # changing date data type into string  
        SA_demand_df[['year','month','day']] = SA_demand_df.date.str.split("-", expand=True) # splitint the date column into 3 new columns titled year month day
        SA_2018_demand_df = SA_demand_df.loc[SA_demand_df['year']== '2018']    # creating the dataframe that contains the information associated with the year of 2018
        SA_2018_demand_df.reset_index(inplace = True)  
        south_africa_2018_demand_df = SA_2018_demand_df.iloc[:, 2:7].copy()    # creating new dataframe not including first two columns at 0 and 1
        
        # changed the values of the hour column ranging from (0,23) to (1,24) using .replace() 
        south_africa_2018_demand_df['hour'] = south_africa_2018_demand_df['hour']+1
        
        south_africa_2018_demand_df = south_africa_2018_demand_df[['hour','day','month','year','system_demand_[mw]']].astype('int')
        south_africa_2018_demand_df.to_csv(self.exported , index=False)                    # exporting a csv file into given directory
        return

    # creating a User-defined function UDF for Tanzania electricity demand data set  
    def clean_TZ(self):
        # for Tanzania data
        """ This function will clean raw data sets in the format of the TZ_Hourly_Load_Generation_Data_2018 xlsx file
            and create a dataframe with the demand,hour,year,month,day columns from the dataset. Then it will export a csv file to your directory. 
            - The arugment 'self.imported' is the path to where you stored your xlsx file with the data set to clean 
            - The argument 'self.exported' is the path to where you want to store the new 'clean' csv file dataframe: 
                        example - '/(your desired directory path)/(name of file).csv' """ 
        path = self.imported 
        TZ_raw_data_df = pd.read_excel(path)
        tanzania_df = TZ_raw_data_df[['DATE','TIME','HG GRAND TOTAL']].copy()              # creating dataframe with desired columns, data, time, and HG Grand total
        tanzania_df.rename(columns={"DATE":"date","TIME":"hour", "HG GRAND TOTAL":"system_demand_[mw]"}, inplace = True) # change the column names in the data frame w/ inplace = True
        
        tanzania_df['date'] = tanzania_df['date'].ffill( axis = 0)                         # using front fill function to fill missing values for the date  
        tanzania_df['date'] = tanzania_df['date'].astype('str')                            # changing date_time data type into string 
        tanzania_df[['year','month','day']] = tanzania_df.date.str.split("-", expand=True) # spliting the date column into 3 new columns titled year month day

        TZ_demand_df = tanzania_df.iloc[:, 1:8].copy()                                     # creating new dataframe not including first column at 0
        TZ_demand_df['hour'] = TZ_demand_df['hour'].astype('str')                          # converting to string to convert to datetime value
        TZ_demand_df['hour'] = pd.to_datetime(TZ_demand_df['hour'])                        # converting hour column from string value to datetime value 
        TZ_demand_df['hour'] = TZ_demand_df['hour'].dt.hour                                # pulling only hour value from datetime value as a float value
        TZ_demand_df['hour'] = TZ_demand_df['hour'].replace(0, 24)                         # Replacing the 0 values with 24 , the time count was 1...23,0
        TZ_demand_df = TZ_demand_df[['hour','day','month','year','system_demand_[mw]']].astype('int')
        TZ_demand_df.to_csv(self.exported, index=False)                                               # exporting a csv file into given directory
        return
    
    # creating a User-defined function UDF of the above code 
    def clean_ZW(self):
        # for Zimbabwe data
        """ This function will clean raw data sets in the format of the ZESA_Hourly_Load_2018_Data xlsx file
            and create a dataframe with the demand,hour,year,month,day columns from the dataset. Then it will export a csv file to your directory. 
            - The arugment 'self.imported' is the path to where you stored your xlsx file with the data set to clean 
            - The argument 'self.exported' is the path to where you want to store the new 'clean' csv file dataframe: 
                        example - '/(your desired directory path)/(name of file).csv' 
            - the argument 'self.year' is the year you want to pull information for in the original spreadsheet in the form of an integer""" 
        zimbabwe_demand_df = pd.DataFrame(columns=['hour', 'day', 'month', 'year', 'system_demand_[mw]'])  # Creating an empty Dataframe with column names only
        selected_year = self.year                                                                                  # year of the selected spreadsheet 
        year = str(self.year)                                                                                      # creating year value as a string for loop 
        path = self.imported                                                                                           # give location of file you want to read inbetween ''
        
        # vector with name of sheet in raw dataset 
        month_year = ("January "+ year,"February "+ year,"March "+ year,
                      "April "+ year,"May "+year,"June "+year,"July "+year,
                      "Aug "+year,"Sept "+year,"Oct "+year,"Nov "+year, "Dec "+year)

        # creating loop that loops through two variables simulanteously 
        for i, m in zip(range(13), range(1,13)):
    
            z_raw_data_df = pd.read_excel(path, sheet_name = month_year[i])               # pulling the second sheet from the xlsx file and automatically turns the results into a dataframe 
            # creating dataframe with desired columns, data, time, and HG Grand total
            zim_df = z_raw_data_df.loc[:, 'Unnamed: 1':'Monthly Peak Demand (MW)'].copy() # picking desired columns by column name
            zim_df = zim_df.loc[:, zim_df.columns != 'Monthly Peak Demand (MW)']          # dropping column titled 'Monthly Peak Demand (MW)'
    
            zim_df.drop(index=[0,25,26], inplace = True , axis = 0)                       # droping rows from dataframe
            zim_demand_df = pd.melt(zim_df, id_vars=['Unnamed: 1'] , var_name='day', value_name='system_demand_[mw]') # using melt function to stack multiple columns into manageable columns
        
            zim_demand_df.insert(2,"month",m)                                     # creating column titled "month" with value m and inserting into the 2 column position
            zim_demand_df.insert(3,"year",self.year)                                      # creating column titled "year" with value 2018 and inserting into the 3 column position

            zim_demand_df.rename(columns = {"Unnamed: 1":"hour"}, inplace = True) # renaming unnamed column with hour 
            zim_demand_df['hour'] = zim_demand_df['hour'].astype('str')           # converting to string to convert to datetime value
            zim_demand_df['hour'] = pd.to_datetime(zim_demand_df['hour'])         # converting hour column from string value to datetime value 
            zim_demand_df['hour'] = zim_demand_df['hour'].dt.hour                 # pulling only hour value from datetime value as a float value
            zim_demand_df['hour'] = zim_demand_df['hour'].replace(0, 24)          # replacing hour values with 0 to 24 
            zimbabwe_demand_df = zimbabwe_demand_df.append(zim_demand_df,ignore_index=True) # appending data frame create for each month to the end of the orginal janurary dataframe 

        zimbabwe_demand_df = zimbabwe_demand_df[['hour','day','month','year','system_demand_[mw]']].astype('int')
        zimbabwe_demand_df.to_csv(self.exported, index=False)                                      # exporting a csv file into given directory
    
    # creating a User-defined function UDF of the above code 
    def clean_MZ(self):
        # for Mozambique data
        """ This function will clean raw data sets in the format of the EDM Hourly_Load_2017_2018_Data xlsx file
            and create a dataframe with the demand,hour,year,month,day columns from the dataset. Then it will export a csv file to your directory. 
            - The arugment 'self.imported' is the path to where you stored your xlsx file with the data set to clean 
            - The argument 'self.exported' is the path to where you want to store the new 'clean' csv file dataframe: 
                        example - '/(your desired directory path)/(name of file).csv' 
            - The argument 'self.year' is the year (in the form of an integer) on the spreadsheet you want to pull information for""" 
        # this loop will append to an empty data frame created below 
        Mozambique_demand_df = pd.DataFrame(columns=['hour','system_demand_[mw]','year','day','month'])  # Creating an empty Dataframe with column names only

        month_start_row = (0,28,56,84,112,140,168,196,224,252,280,308)                                   # the index of the row for when each month starts 
        month_end_column = (33,30,33,32,33,32,33,33,32,33,32,33)                                         # the last column number where each month ends
        year = str(self.year)
        path = self.imported                                                                                         # give location of file you want to read inbetween ''
        # creating loop to clean the data set a few selected rows at a time 
        for i, j in zip(range(0,12), range(0,12)):
            Mozambique_raw_data_df = pd.read_excel(path, sheet_name = year)                              # pulling the second sheet from the xlsx file and automatically turns the results into a dataframe
            
            Moz_df = Mozambique_raw_data_df.iloc[month_start_row[i]:month_start_row[i]+25,:].copy()      # pulling rows 0-25 into a dataframe
            Moz_df = Moz_df.iloc[:, 1:month_end_column[j]]                                               # selecting columns for 1-##
            Moz_df.columns = Moz_df.iloc[0]                                                              # renaming columns with the first row 
            Moz_df = Moz_df.drop(Moz_df.index[0])                                                        # dropping first row 
        
            # 2018 spreadsheet is missing values, so this if statement applies to 2018 spreadsheet  
            if self.year == 2018:
                Moz_df = Moz_df.ffill(axis = 1)                                                          # filling missing NaN values with values in the column infront of it 

            Moz_demand_df = pd.melt(Moz_df, id_vars=['Hour Ending'] , var_name='date', value_name='system_demand_[mw]')  # using melt function to stack multiple columns into manageable columns
            Moz_demand_df['date'] = Moz_demand_df['date'].astype('str')                                  # changing date_time data type into string

            # spliting the date column into 3 new columns titled year month day 
            Moz_demand_df[['year','month','day']] = Moz_demand_df.date.str.split("-", expand=True)
            Moz_demand_df.drop(["date"], axis=1, inplace = True)                                         # droping columns titled data and time
        
            Moz_demand_df['year'] = Moz_demand_df['year'].replace('2004', value = year)
            Moz_demand_df = Moz_demand_df.rename(columns = {'Hour Ending': 'hour'})
        
            Mozambique_demand_df = Mozambique_demand_df.append(Moz_demand_df,ignore_index=True)          # appending data frame create for each month to the end of the orginal janurary dataframe 

        Mozambique_demand_df = Mozambique_demand_df[["hour","day","month","year","system_demand_[mw]"]].astype('int')  # rearranging columns in data frame 
        Mozambique_demand_df.to_csv(self.exported, index=False)                                                     # exporting a csv file into given directory

    # creating a User-defined function UDF of the above code 
    def clean_SZ(self):
        # for Eswatini data
        """ This function will clean raw data sets in the format of the EDM Hourly_Load_2017_2018_Data xlsx file
            and create a dataframe with the demand,hour,year,month,day columns from the dataset. Then it will export a csv file to your directory. 
            - The arugment 'self.imported' is the path to where you stored your xlsx file with the data set to clean 
            - The argument 'self.exported' is the path to where you want to store the new 'clean' csv file dataframe: 
                        example - '/(your desired directory path)/(name of file).csv' 
            - The argument 'self.year' is the year (in the form of an integer) on the spreadsheet you want to pull information for
            - I made corrections on orginal xlsx file for the dates because date 1/13/18-1/20/18 were in a different format than the others, double check dates are in the same format""" 
        path = self.imported                                                                                  # imported xlsx file
        year = str(self.year)                                                                                 # converting c value to string value 
        # creating dataframe
        raw_data = pd.read_excel(path, sheet_name=year)
        data_frame = raw_data.loc[:, ['DATE','TIME','SYST']]
        
        # converting data column into 3 columns [year, day, month] as string
        data_frame = data_frame.astype({"DATE":str})
        data_frame['DATE'] = data_frame['DATE'].str.slice(0,11)
        data_frame[['year','day','month']] = data_frame.DATE.str.split("-",expand=True)
        data_frame = data_frame.drop(['DATE'], axis=1)
        
        # create hour column to replace half hour data, by changing half hour to it's whole hour
        hours_dlb_series = pd.Series(range(1,25)).repeat(2).reset_index(drop = True)                           # creating vector with values 1 -24 
        total_hours = pd.concat([hours_dlb_series]*365, ignore_index=True)                                     # have the vector repeat 365 times to correspond to the number of hours in a year 
        data_frame.loc[:,'TIME'] = total_hours                                                                 # creating new column titled 'hour' with values of the vector = total hours
        
        # create count for every two values to find average load per hour
        double_count = pd.Series(range(8760)).repeat(2).reset_index(drop = True)                               # repeating each value in vector count twice to match half-hour and hour values 
        data_frame['count'] = double_count                                                                     # creating new column 'count' with values = doube_count vector 
        
        # before take average and group by count, convert values to numeric
        data_frame = data_frame.apply(pd.to_numeric)
        group_df = data_frame.groupby('count').mean()                                                           # using group,by function to group by count, taking 17520 values to 8760 values

        final_df = group_df[['TIME','day','month','year','SYST']]\
                    .reset_index(drop = True).rename(columns = {"SYST": "system_demand_[mw]","TIME":"hour"})    # creating data frame with selected columns with index reset, dropping 'count' index 
        final_df = final_df.astype({'hour':int,'day':int, 'month':int, 'year':int})                             # converting date and time columns to interger dtypes
        final_df.to_csv(self.exported, index=False) 
        return

    # creating a User-defined function UDF of the above code 
    def clean_ZM(self):
        # for Zambia data
        """ This function will clean raw data sets in the format of the SACREE RE Project Data Collection ZESCO xlsx file
            and create a dataframe with the demand,hour,year,month,day columns from the dataset. Then it will export a csv file to your directory. 
            - The arugment 'self.imported' is the path to where you stored your xlsx file with the data set to clean 
            - The argument 'self.exported' is the path to where you want to store the new 'clean' csv file dataframe: 
                        example - '/(your desired directory path)/(name of file).csv' 
            - This function does not include data from the year 2017 or 2019 which are located on the spreadsheet"""   
        path = self.imported
        zambia_raw_data_df = pd.read_excel(path, sheet_name = "Demand Data")     # pulling the second sheet from the xlsx file and automatically turns the results into a dataframe 
        
        zambia_df = zambia_raw_data_df.drop(zambia_raw_data_df.index[0:26])                   # dropping 0-26 from raw data set 
        zambia_demand_df = zambia_df[['Unnamed: 1','Unnamed: 5']]                             # creating dataframe with selected columns
        zambia_demand_df = zambia_demand_df.drop(zambia_demand_df.index[0:3])                 # dropping first 3 rows 
        zambia_demand_df.rename(columns={"Unnamed: 1":"hour_per_year", "Unnamed: 5":"system_demand_[mw]"}, inplace = True) # renaming columns
        zambia_demand_df = zambia_demand_df.reset_index(drop=True)                            # reseting index and droping old index 
        
        zam_list = []                            # empty list to store dates generated by loop
        # Creating values for loop to build date column with dates ranging from 1-1-2018 to 12-31-2018 
        start_date = date(2018, 1, 1)            # start date for column
        end_date = date(2018, 12, 31)            # end date for column 
        delta = end_date - start_date            # as timedelta for loop

        # loop to print date starting from 1-1-2018 and store into zam_list 
        for i in range(delta.days + 1):
            day = start_date + timedelta(days=i) # building date with i iterations
            zam_list.append(day)                 # adding to empty list 
        
        zambia_series = pd.Series(zam_list)      # building series to repeat dates to match hours in a year
        zambia_repeat = zambia_series.repeat(24).reset_index(drop = True)   # repeat each date 24 times to much hours, totla 8760 hours
        zambia_date_df = pd.DataFrame({'date': zambia_repeat})              # creating zam list into "date" dataframe  
        zambia_demand_df.insert(1,"date",zambia_date_df)                    # adding date column to zambia demand df 
        
        # creating values for the hour column in the data frame 
        hours_day = pd.Series(range(1,25))       # making a vector of the values 1-24 
        hours = pd.concat([hours_day]*365, ignore_index=True)               # have the vector repeat 365 times to correspond to the number of hours in a year 
        zambia_demand_df['hour'] = hours         # creating column named hours with the repeating value 1-24 'hours' for each day in each month of the year 

        zambia_demand_df = zambia_demand_df.drop(zambia_demand_df.index[8760])                          # drop last row in dataframe because it wasn't needed 
        zambia_demand_df['date'] = zambia_demand_df['date'].astype('str')                               # changing date data type into string 
        zambia_demand_df[['year','month','day']] = zambia_demand_df.date.str.split("-", expand=True)    # spliting the date column into 3 new columns titled year month day 
        zambia_demand_df = zambia_demand_df[['hour','day','month', 'year', 'system_demand_[mw]']].astype('int')       # rearranging columns and created updated dataframe 
        
        zambia_demand_df.to_csv(self.exported, index=False)                            # exporting a csv file into given directory
        return

    # creating a User-defined function UDF of the above code 

    def clean_MW(self):
        # for Malawi
        """ This function will clean raw data sets in the format of the HOURLY TOTALS GENERATED APRIL 2018.xlsx file found in the malawi_data folder
            and create a dataframe with the demand,hour,year,month,day columns from the dataset. Then it will export a csv file to your directory. 
            - The arugment 'self.imported' is the path to which folder you stored your xlsx file with the data set to clean 
            - The argument 'self.exported' is the path to where you want to store the new 'clean' csv file dataframe: 
                        example - '/(your desired directory path)/(name of file).csv' 
            - Make sure the files in each folder in the malawi data called (data_20xx) are sorted by name. 
                (The first file should be the one for april, last file should be the one fore september) 
            - I made corrections on orginal xlsx files by making adjustments to file name, sheet name so that all files can be in the same format
            - I also made corrects to missing values in the original data sets by taking
                the average between days (for missing values for a day) and hours (for missing values for certain hours)
            - This function cleans each data_20xx folder in the malawi data folder seperately"""
        malawi_demand_df = pd.DataFrame(columns=['hour', 'day', 'month', 'year', 'system_demand_[mw]'])  # Creating an empty Dataframe with column names only
        
        # Creating loop that list all files in the selected directory
        # files are then read in and then can run code to clean each file 
        
        entries = os.listdir(self.imported)
        month_days = (30,31,31,28,31,31,30,31,31,30,31,30)
        
        for i, entry in zip(range(12), entries):
            path_pt1 = self.imported+'/'
            path_pt2 = entry
            path = str(entry)
            malawi_month_df = pd.read_excel(path_pt1+path)     # pulling the second sheet from the xlsx file and automatically turns the results into a dataframe 
            
            malawi_raw_data = malawi_month_df.iloc[4:53,].copy() #creating data frames with the rows from row 4 to row 52 
        
            # deleting header and moving all rows up 
            new_header = malawi_raw_data.iloc[0] #grab the first row for the header
            malawi_raw_data = malawi_raw_data[1:] #take the data less the header row
            malawi_raw_data.columns = new_header #set the header row as the df header
            
            month_data_df = malawi_raw_data.reset_index(drop =True) # reseting index and with new name data frame 
            
            # need to do this for all columns
            month_demand_df = pd.melt(month_data_df, id_vars=['TIME'] , var_name='date', value_name='system_demand_[mw]')
            
            # changing date_time data type into string 
            month_demand_df['date'] = month_demand_df['date'].astype('str') 
            
            # spliting the date column into 3 new columns titled year month day 
            month_demand_df[['year','month','day']] = month_demand_df.date.str.split("-", expand=True)

            # This needs to be adjusted to each month because they have different total number of days
            hours = pd.Series(range(1,25))
            hours_set = hours.repeat(2).reset_index(drop = True)
            total_hours = pd.concat([hours_set]*month_days[i], ignore_index=True) # have the vector repeat 31 times to correspond to the number of hours in a month 

            month_demand_df.loc[:,'hour'] = total_hours # creating hour column with double hour count 
            
            # Creating a count to use for group.by funciton
            # range is total number of hours in a month, this will be different for each month 
            count = pd.Series(range(24*month_days[i])) # different for each month 
            double_count = count.repeat(2).reset_index(drop = True)
            
            month_demand_df['count'] = double_count # creating count column to use for group.by function 
            
            # converting day, month and year columns into numeric values to use mean() for groupby ()
            month_demand_df['day'] = pd.to_numeric(month_demand_df.day)
            month_demand_df['month'] = pd.to_numeric(month_demand_df.month)
            month_demand_df['year'] = pd.to_numeric(month_demand_df.year)
            month_demand_df['system_demand_[mw]'] = month_demand_df['system_demand_[mw]'].astype('int')
            
            b_groupby = month_demand_df.groupby('count').mean() # using groupby function to average half hour time demand to hour time demand

            month_demand_df = b_groupby[['hour','day','month','year','system_demand_[mw]']].reset_index(drop = True) # rearranging columns to match desired format

            month_demand_df = month_demand_df.astype('int') # making all columns in the data frame into int values to be consistant 
            
            malawi_demand_df = malawi_demand_df.append(month_demand_df,ignore_index=True) # appending data frame create for each month to the end of the orginal janurary dataframe 
            
            malawi_demand_df = malawi_demand_df.sort_values(by=['year','month', 'day','hour'])
            
        malawi_demand_df.to_csv(self.exported, index=False)                                    # exporting a csv file into given directory

    # creating a User-defined function UDF of the above code 
    def clean_AO(self):
        """ This function will clean raw data sets in the format of the Lesotho_Load_Profile_2017_2019 xlsx file
            and create a dataframe with the demand,hour,year,month,day columns from the dataset. Then it will export a csv file to your directory. 
            - The arugment 'self.imported' is the path to where you stored your xlsx file with the data set to clean 
            - The argument 'self.exported' is the path to where you want to store the new 'clean' csv file dataframe: 
                        example - '/(your desired directory path)/(name of file).csv' """ 
        path = self.imported
        Angola_raw_data = pd.read_csv(path) # importing csv file with Angola raw dataset 
        Angola_demand = Angola_raw_data.iloc[3:369,1:27] # creating dataframe selecting desired rows and columns
        Angola_demand = Angola_demand.reset_index(drop = True) # reseting index

        new_header = Angola_demand.iloc[0] # making first row into header for dataframe
        Angola_demand = Angola_demand[1:] # making dataframe into every row after first row
        Angola_demand.columns = new_header # inserting new header into dataframe
        
        Angola_demand = Angola_demand.drop(columns = 'Dia') # dropping column called 'Dia'
        Angola_demand = Angola_demand.set_index('Data') # making data column into index column to apply stack funciton
        new_Angola_demand_df = Angola_demand.stack() #using stack function to sack desired columns into one column with corresponding hour
        Angola_demand_2018 = new_Angola_demand_df.to_frame() # changing data set type into a dataframe

        Angola_demand_2018 = Angola_demand_2018.rename(columns={0:"system_demand_[MW]"}) # renaming columns in dataframe
        Angola_demand_2018 = Angola_demand_2018.reset_index() # reseting index to make date column into first column of dataset
        Angola_demand_2018 = Angola_demand_2018.rename(columns = {"Data":"date",0:"hour"}) # renaming columns in dataframe
        Angola_demand_2018["date"].astype(str) # changinging 'date' column into string to split date into 3 columns
        
        # spliting date column into 3 columns divided by / to have a month, day and year column
        Angola_demand_2018[['month','day','year']] = Angola_demand_2018.date.str.split("/",expand=True,)
        Angola_demand_2018['hour'] = Angola_demand_2018['hour'].astype(int) # changing sting data type into int data type
        Angola_demand_2018['hour'] = Angola_demand_2018['hour']+1 # changing hour column from 0-23 to 1-24
        
        Angola_demand_2018['year'] = Angola_demand_2018['year'].astype(int) # changing year column into int data type
        Angola_demand_2018['year'] = Angola_demand_2018['year']+2000 # chaning year column value from 18 to 2018
        
        Angola_demand_2018['system_demand_[MW]'] = Angola_demand_2018['system_demand_[MW]'].astype(str) # change column to string value to take out comma
        Angola_demand_2018['system_demand_[MW]'] = Angola_demand_2018['system_demand_[MW]'].str.replace(',', '') # removing comma from data values
        # rearranging columns in dataframe 
        Angola_demand_2018 = Angola_demand_2018[['hour','day','month','year','system_demand_[MW]']] # rearranging columns in dataset 
        Angola_demand_2018[['hour','day','month']] = Angola_demand_2018[['hour','day','month']].astype(int) # changing columns into int values
        Angola_demand_2018['system_demand_[MW]'] = Angola_demand_2018['system_demand_[MW]'].astype(float) # converting column to float value because it has values after the decimal                                                                

        Angola_demand_2018.to_csv(self.exported, index=False)                                      # exporting a csv file into given directory
        return 
        
    def testing(self):
        print("Connected to re_func module")
        print(self.imported, self.exported, self.year)
           
 

        
 




 