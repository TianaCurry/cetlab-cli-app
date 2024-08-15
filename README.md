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

**The virtual environment I created was "cetlab-cli"; and I directly imported the following <u>libraries</u>:**

- numpy
- pandas
- os
- sys
- argparse
- datetime

**I built two modules**

- `re_cli`: creates commandline application functionality
- `re_func`: holds data wrangling functions

### Running commands

1. start will the help command to view all command options and for momre details on the functions

```bash
% ./re_cli.py -h
```

![run ./re_cli.py -h command](https://github.com/TianaCurry/cetlab-cli-app/blob/b0dfea656f0face8422ce55f919bb12e49f33dc1/images/Screenshot%202024-08-13%20at%209.58.16%E2%80%AFPM.png)


2. check if your raw data fits the strict format structure for the functions

3. selected function by country two letter code name in the format `clean_<county-abbreviation>`
4. run command using mock data
5. follow prompt (if provided)
6. locate output dataframe in current working directory under the format `<input-file-name>-dataframe.csv`