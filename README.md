# repaire_task_uno

## Background
Millions of users flood to stackoverflow to have their questions addressed or help those who want their questions answered. I sought to address only a small portion of those users, focusing one taking the URL of any individual and comparing it against the Melbourne, Australia cohort.

## Task
In this task, I created an application where you run the stackoverflow_melb.py file and the 'QueryResults.csv' file is automatically downloaded. You then run the user_comparison.py file where you'll be prompted for a user url. Once you've entered the url you'll receive a response along these lines:
"https://stackoverflow.com/users/696257/dkulkarni is in the top # percent of Melbourne Stackoverflow users based on reputation"

The link will be the one you provided and the calculation will come as a result of processing the information from the individual link and comparing that reputation score with the broader Melbourne cohort's reputation scores. 

## Implementation
This package has been built for Python 3.0+
If you don't have it downloaded you can download the latest version at https://www.python.org/downloads/

Be sure to install the following packages using the pip install <package name> method:
  - selenium
  - bs4
  - requests
  - pandas
  - ChromeDriverManager

The order is important.
First run the stackoverflow_melb.py file.
The code will be some offshoot of the following:<br />
<code>python .\stackoverflow_melb.py</code>

As a result a file titled 'QueryResults.csv' will automatically download. Be sure to move this into your code's current working directory before proceeding. Otherwise the rest of your code won't work

Then run the next file with code that looks like this:<br />
<code>python .\user_comparison.py</code>

When prompted put in a url and let the magic happen.

### That's all she wrote folks!
