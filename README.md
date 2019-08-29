## Data

#### By Shirley Keter ,Aug 2019

## Description
#### App that retrieves that data and stores it in an SQLite dB table showing start date , end date and value.


## Set Up and Installations


### Prerequisites
* Ubuntu Software
* Python3.6
* Postgres
* python virtualenv
* Clone the Repo
* Run the following command on the terminal: git clone https://github.com/chiriket/Month-Data.git && cd data

### Activate virtual environment
* Activate virtual environment using python3.6 as default handler

### Install dependancies
Install dependancies that will create an environment for the app to run pip3 install -r requirements.txt

### Create the Database
* import sqlite3
* conn = sqlite3.connect('data.db') 

### Create .env file.

### Run initial Migration
* python3.6 manage.py makemigrations gram
* python3.6 manage.py migrate
* Run the app
* python3.6 manage.py runserver
* Open terminal on localhost:8000

## Known bugs
There are no known bugs.

## Technologies used
- Python 3.6
- HTML
- Bootstrap 4
- SQLite3
-
- 

## Support and contact details
Contact me on shirleyketer@gmail.com.

## License
Copyright (c) Shirley Keter
