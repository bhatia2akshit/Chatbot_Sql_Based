# Chatbot_Sql_Based
Created a chatbot based on html, css, js and used GPT3 to covert text into sql and used pandasql to convert sql into pandas dataframe conditions.


## General Information
Ensure the installation of flask, python and the python packages {openai, pandas, pandasql} onto the local environment.

## API Key
1. Then, it is essential to obtain the openai api key. The process is very simple. Go to the website: https://platform.openai.com/account/api-keys
2. Generate your key.
3. Copy the key in the file app.py (line 7) in the variable openai.api_key.

## Running Instructions
To run the chatbot, on the terminal, in the path of the root folder (ie the folder on which the folders {static, templates} and the file app.py exist, type the command: 'flask run'

The chatbot is visible on the localhost:5000 (usually).

First, load the csv file. At the moment, only csv file is supported. Click on the button "Load the file". There will be no message. Although, in the python console, where flask run is typed, there will be a message "file is loaded".

Then, start asking questions to the chatbot.

## Exception related to SQLAlchemy time.clock issue.
To solve this issue, find the compat.py of SQLAlchemy package in the file explorer. In my system, it is located at: lib\site-packages\sqlalchemy\util\compat.py

In the file compat.py, replace time.clock() with time.time().

The issue should be resolved with this.
