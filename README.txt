This is README.

CSV Validator is a program which can be used to validate and create different CSV files based on given rules and
conditions in the problem.
The CSV Validator creates two files- valid.csv and invalid.csv. The valid.csv file contains all the data which is true
for all the provided conditions in program. The invalid.csv file contains all the data which is false for all the provided conditions in program.

The rules for a file to be categorized as valid are as follows:
●	The video title must be shorter than 30 characters.
●	The video must have over 10 likes.
●	The video must have over 200 sales.
●	The video price must be under 20 Euros or under 25 Canadian Dollars. (videos.csv only lists prices in USD, so we've also provided exchange_rates.csv, which includes exchange rates from USD to other currencies.)

The program has been written in Python v2.7. Following are the steps to run the program:
Step 1- Download Python v2.7
Step 2- You can use absolute path or relative path. Please run the following command in the command prompt once you enter the
        CSVValidator directory with the given arguments:

        python run_validator.py data/videos.csv data/exchange_rates.csv

Step 3- The command prompt displays the Grand total of the unit_price_in_usd of the valid.csv file
