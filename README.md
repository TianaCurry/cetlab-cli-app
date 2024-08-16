# cetlab-cli-app

## Table of Contents

+ Overview
+ Background
+ How-to Guide
  + Dependencies
  + Running Commands

## Overview

This program was developed using Python and is a data wrangling command line interface app to clean, structure, and transform energy demand (load) data for 10 Southern African countries; for the UC Santa Barbara Bren School Clean Energy Transformation lab (CETlab) research team. This program was completely designed, developed and maintain by the Software Engineer, Data Scienctist Tiana Curry. Which solved data pipeline issues for the CETlab by automating the data wrangling process.

## Background

This program is a command line interface application (cli app) and is designed to clean datasets for the CETlab GridPath software working in collaboration with specific electricity to companies throughout Southern Africa. The goal is to automate the data wrangling, cleaning and structuring process for the data coming from these specific agencies. That provides a very simply user experience, where users can simply input their raw datasets and output a clean tabular dataframe perfect for predictive and Machine Learning Models. CETlab and GridPath goal is to provide sustainable and reliable renewable energy to 10+ countries throughout Africa, to support their growing economies and increase access to essential resources; while leading the way for clean energy use for large populations.

The results of this CETlab cli app was an increase in efficiency and accuracy while contributing an algorithm that's reusable, reproducible, and utilize by the entire CETlab. The CETlab cli app currently provides data wrangling functions for electricity companies in the following Southern African countries: Angola, Eswatini, Lesotho, Malawi, Mozambique, Namibia, South Africa, Zambia, Zimbabwe. Each electricity company had very differnt was of storing and documenting their data which resulted in creating different algorithms tailered to their data documenting methods.

The data used in the CETlab is private and not accessible to the public in anyway, and so a mock dataframe was created and provided using random data points to show functionality of this program. A test input dataset and clean dataframe was provided to test the Eswatini function to show full use of the cli app. You can find the mock data and dataframe results in the test-data directory.

Below is a how-to guide on what commands and functions are available to use, including data wrangling functions for all 10 countries, and test functions to see simple functionality. To view only the functions for data cleaning you can access this information in the Data Wrangling Functions Jupyter notebook. The complete source code for the cli app can be found in the src directory which includes two main scripts the `re_cli.py` script for command line functionality and the `re_func.py` script for data wrangling functions.

The CETLab cli app is an example of an idea to deployment, full stack, Object-Oriented Program Python application that solves common organization issues in data pipeline development for real world use.

## How to Guide

### Dependencies

```bash
Python==3.12.3
code==1.91.1
```

#### You can find the following dependencies in the requirements.txt file

```bash
DateTime==5.5
et-xmlfile==1.1.0
numpy==2.0.1
openpyxl==3.1.5
pandas==2.2.2
python-dateutil==2.9.0.post0
pytz==2024.1
setuptools==72.2.0
six==1.16.0
tzdata==2024.1
zope.interface==7.0.1
```

##### The virtual environment I created was "cetlab-cli"; and I directly imported the following <u>libraries</u>:

+ numpy
+ pandas
+ os
+ sys
+ argparse
+ datetime

##### I built two modules

+ `re_cli`: creates commandline application functionality
+ `re_func`: holds data wrangling functions

### Running commands

#### 1. Check if your raw data fits the strict format structure for the functions. There are four main things to check:

- **the column names**
- **data enteries contain a load demand per half hour**
- **the number of rows**
- **the name for each sheet.**

<br>
a. Make sure you have four columns with the following column names 'WEEK', 'DAY', 'DATE', 'TIME', 'SYST'.
<br>
<br>
<img src="./__md-pics/2-input-columns-names.png" alt="" width="300"/>
<br>
<br>
b. Starting from Jan 1, 20xx to Dec 31, 20xx, there should be an entry for every every half hour for every day of the year in the following format
<br>
<br>
<img src="./__md-pics/3-load-by-half-hour.png" alt="" width="300"/>
<br>
<br>
c. The number of rows should be 17521
<br>
<br>
<img src="./__md-pics/4-total-rows.png" alt="" width="300"/>
<br>
<br>
d. The 'DATE' column is day/month/year in the format dd/mm/yyyy
<br>
<br>
<img src="./__md-pics/5-date-in-format-ddmmyyyy.png" alt="" width="300"/>
<br>
<br>
e. The sheet name should be a four digit year.
<br>
<br>
<img src="./__md-pics/6-sheet-name-as-year.png" alt="" width="300"/>

#### 2. start will the help command to view all command options and for momre details on the functions

```bash
% ./re_cli.py -h
```

<br>
<img src="./__md-pics/7-cli-options-country-codes.png" alt="" width="600"/>

#### 3. We can see the command options with a more detailed description, to use the mock dataset we will use the function with the command `-sz` `--eswatini`.

<br>
<img src="./__md-pics/8-desired-function-details.png" alt="" width="600"/>

#### 4. Run command using mock data. We'll use the function by country two letter code name to run the command

```bash
Syntax: % ./re_cli.py <file-name> -<county-code>
```

<br>
<img src="./__md-pics/9-run-data-wrangling-function.png" alt="" width=""/>

#### 5. follow prompt (if provided). For the Eswatini function the prompt will be the enter the year of the Excel file sheet

<br>
<img src="./__md-pics/10-prompt-input.png" alt="" width=""/>

#### 6. Three prompts will popup if your entry is validated, indicating the data cleaning process has began. And you can locate output dataframe in current working directory under the format `<input-file-name>-dataframe.csv`

<br>
<img src="./__md-pics/11-verifying-input-vallues.png" alt="" width=""/>

#### 7. View final clean tabular dataframe, ready for further analysis. Each dataframe has the same format for all countries with the following columns: 'hour', 'day', 'month', 'year', 'system_demand[mw]'

<br>
<img src="./__md-pics/12-results-desired-column-names.png" alt="" width="450"/>
