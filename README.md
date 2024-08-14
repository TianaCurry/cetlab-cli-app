# cetlab-cli-app

A data wrangling command line interface app to clean, structure, and transform energy demand (load) data for 10 Southern African countries; for the UC Santa Barbara Bren School CETlab research team

## Background

## How to Guide

### Dependencies

```bash
Python==3.12.3
code==1.91.1
```

**You can find the following dependencies in the requirements.txt file**

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


2. check if your raw data fits the strict format structure for the functions
3. selected function by country two letter code name in the format `clean_<county-abbreviation>`
4. run command using mock data
5. follow prompt (if provided)
6. locate output dataframe in current working directory under the format `<input-file-name>-dataframe.csv`