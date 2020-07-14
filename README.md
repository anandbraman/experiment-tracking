# experiment-tracking

Welcome to my short and simple experiment tracking script. I primarily use this script for tracking the results of hyperparameter tuning experiments across various models. I wrote this script because I found recording the results of hyperparameter tuning to be pretty tedious if you're doing it by hand. At first, I thought about just writing results to a pandas DataFrame or csv and saving it locally. But 1) I'd never used Google Drive or Sheets API before and 2) sharing the spreadsheet with collaborators easy and convenient. My managers + coworkers can take a look at what models are working best in real time! 

## Setup
Before being able to use this scipt or replicating something like it for yourself, head over to https://gspread.readthedocs.io/en/latest/oauth2.html and follow the steps for authentication. Make sure you share the spreadsheet with the client email.

## Usage

`experiment_tracker.py` implements the ExperimentTracker class. To initialize, provide the filepath to the `client_secret.json`, the name of the spreadsheet, and the names of the parameters/results you would like to track. The defualt worksheet argument is 'Sheet1', which is Google's default worksheet name but you can set that to something else if you like. The 'worksheet' is the tab at the bottom when you open a Google Sheet. 

First row of the spreadsheet the names of the parameters/results you want to track and the experiment-tracking module is ready to use.

