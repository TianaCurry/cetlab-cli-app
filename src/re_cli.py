#!/usr/bin/env python3

# libraries
import os
import sys
import argparse

# my module
import re_func

class Singleton:
    def __init__(self, file_arg=None, year_arg=None):
        self.file = file_arg
        self.year = year_arg
        self.cwd = os.getcwd()
        self.df = f'{self.cwd}/{self.file[0:-4]}-dataframe.csv' if self.file != None else f'{self.cwd}'

        # messages
        self.df_location_msg = f'Exporting to: "{self.df}"'
        self.enter_path_msg = "Please enter a path to desired dataset..."
        self.cleaning_msg = 'Cleaning data...'
        self.path_dne_msg = "Path does not exist..."
        self.enter_digits_msg = "Please enter year as 4 digit integer to start cleaning dataset..."
    
    def create_parser(self):
        parser = argparse.ArgumentParser(
            prog='re_cli',
            #usage='./re_cli.py <file-path> [options]'
            description="""
              Renewable Energy Command line App:
              Welcome to Energy Demand Dataframe Tool for the UC Santa Barbara CETlab and the GridPath Software...\n
              Commandline format: ./re_cli.py <file-path> [options]
            """,
            epilog="""
              There's a function for each researched country in Southern Africa.
              The functions are set to pull the demand informaiton for the year 2018.
              Functions export csv files in format: path/<input-file-name>-dataframe.csv
            """,
        )

        # positional arguments
        parser.add_argument("file", help="path of file to desired raw dataset, positional arguments")
        
        # optional arguments
        
        # official optional arguments
        parser.add_argument("-ao", "--angola", action="store_true", help=
              """This function will clean raw data sets in the format of the Lesotho_Load_Profile_2017_2019 xlsx file
                 and create a dataframe with the demand,hour,year,month,day columns from the dataset. Then it will export a csv file to your directory. 
                   - The arugment 'self.imported' is the path to where you stored your xlsx file with the data set to clean 
                   - The argument 'self.exported' is the path to where you want to store the new 'clean' csv file dataframe: 
                        example - '/(your desired directory path)/(name of file).csv'"""
        )
        parser.add_argument("-sz", "--eswatini", action="store_true", help=
              """ This function will clean raw data sets in the format of the EDM Hourly_Load_2017_2018_Data xlsx file
                  and create a dataframe with the demand,hour,year,month,day columns from the dataset. Then it will export a csv file to your directory. 
                    - The arugment 'self.imported' is the path to where you stored your xlsx file with the data set to clean 
                    - The argument 'self.exported' is the path to where you want to store the new 'clean' csv file dataframe: 
                        example - '/(your desired directory path)/(name of file).csv' 
                    - The argument 'self.year' is the year (in the form of an integer) on the spreadsheet you want to pull information for
                    - I made corrections on orginal xlsx file for the dates because date 1/13/18-1/20/18 were in a different format than the others, double check dates are in the same format"""
        )
        parser.add_argument("-ls", "--lesotho", action="store_true", help=
              """ This function will clean raw data sets in the format of the Lesotho_Load_Profile_2017_2019 xlsx file
                  and create a dataframe with the demand,hour,year,month,day columns from the dataset. Then it will export a csv file to your directory. 
                    - The arugment 'self.imported' is the path to where you stored your xlsx file with the data set to clean 
                    - The argument 'self.exported' is the path to where you want to store the new 'clean' csv file dataframe: 
                        example - '/(your desired directory path)/(name of file).csv'"""
        )
        parser.add_argument("-mw", "--malawi", action="store_true", help=
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
        )
        parser.add_argument("-mz", "--mozambique", action="store_true", help=
              """ This function will clean raw data sets in the format of the EDM Hourly_Load_2017_2018_Data xlsx file
                  and create a dataframe with the demand,hour,year,month,day columns from the dataset. Then it will export a csv file to your directory. 
                    - The arugment 'self.imported' is the path to where you stored your xlsx file with the data set to clean 
                    - The argument 'self.exported' is the path to where you want to store the new 'clean' csv file dataframe: 
                        example - '/(your desired directory path)/(name of file).csv' 
                    - The argument 'self.year' is the year (in the form of an integer) on the spreadsheet you want to pull information for"""
        )
        parser.add_argument("-na", "--namibia", action="store_true", help=
              """ This function will clean raw data sets in the format of the NA_Hourly_Load_Generation_Imports_2018 xlsx file
                  and create a dataframe with the demand,hour,year,month,day columns from the dataset. Then it will export a csv file to your directory. 
                    - The arugment 'self.imported' is the path to where you stored your xlsx file with the data set to clean 
                    - The argument 'self.exported' is the path to where you want to store the new 'clean' csv file dataframe: 
                        example - '/(your desired directory path)/(name of file).csv' """
        )
        parser.add_argument("-za", "--southafrica", action="store_true", help=
              """ This function will clean raw data sets in the format of the Eskom_RSA_Load_RE_Jan_2016_Jun_2019 xlsx file
                  and create a dataframe with the demand,hour,year,month,day columns from the dataset. Then it will export a csv file to your directory. 
                    - The arugment 'self.imported' is the path to where you stored your xlsx file with the data set to clean 
                    - The argument 'self.exported' is the path to where you want to store the new 'clean' csv file dataframe: 
                        example - '/(your desired directory path)/(name of file).csv' """
        )
        parser.add_argument("-tz", "--tanzania", action="store_true", help=
              """ This function will clean raw data sets in the format of the TZ_Hourly_Load_Generation_Data_2018 xlsx file
                  and create a dataframe with the demand,hour,year,month,day columns from the dataset. Then it will export a csv file to your directory. 
                    - The arugment 'self.imported' is the path to where you stored your xlsx file with the data set to clean 
                    - The argument 'self.exported' is the path to where you want to store the new 'clean' csv file dataframe: 
                        example - '/(your desired directory path)/(name of file).csv' """
        )
        parser.add_argument("-zm", "--zambia", action="store_true", help=
              """ This function will clean raw data sets in the format of the SACREE RE Project Data Collection ZESCO xlsx file
                  and create a dataframe with the demand,hour,year,month,day columns from the dataset. Then it will export a csv file to your directory. 
                    - The arugment 'self.imported' is the path to where you stored your xlsx file with the data set to clean 
                    - The argument 'self.exported' is the path to where you want to store the new 'clean' csv file dataframe: 
                        example - '/(your desired directory path)/(name of file).csv' 
                    - This function does not include data from the year 2017 or 2019 which are located on the spreadsheet"""
        )
        parser.add_argument("-zw", "--zimbabwe", action="store_true", help=
              """ This function will clean raw data sets in the format of the ZESA_Hourly_Load_2018_Data xlsx file
                  and create a dataframe with the demand,hour,year,month,day columns from the dataset. Then it will export a csv file to your directory. 
                    - The arugment 'self.imported' is the path to where you stored your xlsx file with the data set to clean 
                    - The argument 'self.exported' is the path to where you want to store the new 'clean' csv file dataframe: 
                        example - '/(your desired directory path)/(name of file).csv' 
                    - the argument 'self.year' is the year you want to pull information for in the original spreadsheet in the form of an integer"""
        )
        
        # testing optional arguments
        parser.add_argument("-t", "--tester", metavar="", help="test, tester command with second required input, options") # command/event/action object
        parser.add_argument("-re", "--repeat", action="store_true", help="test, repeats file value") 
        parser.add_argument("-c", "--check", action="store_true", help="test, check if positional argument is a valid path, with alerts")
        parser.add_argument("-i", "--input", action="store_true", help="test, prompts you to enter a year if used")
        parser.add_argument("-t2", "--tester2", action="store_true", help="test, testing connection to re_func module")

        return parser
           
    def check_path(self):
        if self.file == None:                             # methods 
            print(self.enter_path_msg)                    #raise Exception(self.enter_path_msg)
        elif os.path.exists(self.file) == False:
            print(self.path_dne_msg, self.enter_path_msg) #raise Exception(self.path_dne_msg, self.enter_path_msg)
        else:
            print(self.df_location_msg)
            print(self.cleaning_msg)

    def check_year(self):
        if self.year == None:
            print('No year entered...', self.enter_digits_msg)
        elif type(self.year) is int and len(str(self.year)) == 4:
            print('Date confirmed...')
        else:
            print('Invalid year entered...', self.enter_digits_msg)

def main():
    parser = Singleton().create_parser()
    args = parser.parse_args()

    # testing argument commands
    if args.tester:
        print("Tester activated...")
        print('testing:',args.file)
        print('testing:',args.tester)

    elif args.file and len(sys.argv) == 2:                # and not args.repeat and not args.check
        print('echo:',args.file)

    elif args.repeat:
        print('Repeating file...')
        print('repeated:', args.file)

    elif args.check:
        print('checking path...')
        Singleton(args.file).check_path()
        print(Singleton(args.file).df)

    elif args.input:
        try:
            year = int(input("Enter desired year:"))
        except ValueError:
            print(Singleton().enter_digits_msg)
        else:
            print(f"The year is {year}")
            Singleton(year_arg=year).check_year()

    elif args.tester2:
        try:
            year = int(input("Enter desired year:"))
        except ValueError:
            print(Singleton().enter_digits_msg)
        else:
            print(f"The year is {year}")
            Singleton(year_arg=year).check_year()
            Singleton(args.file).check_path()
            re_func.ReDataframes(imported=args.file, exported=Singleton(args.file).df, year=year).testing()

    # official argument commands
    elif args.eswatini or args.mozambique or args.zimbabwe:
        try:
            year = int(input("Enter desired year:"))
        except ValueError:
            print(Singleton().enter_digits_msg)
        else:
            Singleton(year_arg=year).check_year()
            Singleton(args.file).check_path()

            values = re_func.ReDataframes(imported=args.file, exported=Singleton(args.file).df, year=year)

            if args.eswatini:
                values.clean_SZ()
            elif args.mozambique:
                values.clean_MZ()
            elif args.zimbabwe:
                values.clean_ZW()
    
    else:
        values = re_func.ReDataframes(imported=args.file, exported=Singleton(args.file).df)

        if args.lesotho:
            values.clean_LS()
        elif args.namibia:
            values.clean_NA()
        elif args.southafrica:
            values.clean_ZA()
        elif args.tanzania:
            values.clean_TZ()
        elif args.zambia:
            values.clean_ZM()
        elif args.malawi:
            values.clean_MW()
        elif args.angola:
            values.clean_AO()

# execute
if __name__ == "__main__":
    main()