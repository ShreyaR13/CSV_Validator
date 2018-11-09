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




Following are the answers to the questions provided-
1.	Was the question/problem clear? Did you feel like something was missing or not explained correctly?
I think that the question was pretty clear. The rules and guidelines were explained precisely and thus it was easier to
understand and implement the solution for the given problem.

2.	What makes your solution awesome?
I think there are several factors which makes my solution awesome:
•	I was able to implement all the given conditions and rules expected
•	I was able to handle the memory management issue if in near future the file provided for the problem was large in size.
    I handled it by using generator. The function reads CSV row one by one. This helps to read large CSV files.
    It reads them in chunks. I used generator because while performing a file-system search, a user would be happier to
    receive results on-the-fly, rather the wait for a search engine to go through every single file and only afterwards return results.
•	I made sure the errors are handled in advance by providing user the appropriate explanation, so that the user knows
    which incorrect input by the user terminated the execution of the program.

3.	Did you have to make any trade-offs in your design? If so, what?
I tried my best that my design doesn’t have any trade-offs. I have tried to address all the conditions and possible errors in advance.

4.	Is there anything else you want to share about your solution or the problem?
I have tried by best to address all the possible conditions and rules for the solution. I hope it meets your expectations.
