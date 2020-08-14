import mysql.connector
import matplotlib
from matplotlib import pyplot as plt
import pandas as pd
from pandas import DataFrame
from pandastable import Table

def pop_db():
    colums = ["OBJECTID", "ISO_CODE", "COUNTRY_NAME", "Date", "NewCase", "TotalCase", "NewDeath", "TotalDeath"]

    mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "1d0n7n33d1MSQL",
    database = "coviddata",
    )

    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM coviddata.coviddata WHERE Date = '2020-04-23T00:00:00.000Z'")
    data = cursor.fetchall()
    mydb.close()

    return colums, data

def display_cases():
    df_colums, db_data = pop_db()
    data_df = pd.DataFrame(db_data, columns=df_colums).set_index("OBJECTID")
    
    data_df.plot(kind='bar',x='COUNTRY_NAME',y='TotalCase')

    plt.show()  

def display_deaths():
    df_colums, db_data = pop_db()
    data_df = pd.DataFrame(db_data, columns=df_colums).set_index("OBJECTID")
    
    data_df.plot(kind='bar',x='COUNTRY_NAME',y='TotalDeath')

    plt.show()  

running = True
type = ""

while running:
    type = input('Select what data you would like to see. Insert "1" for Total Cases. Insert "2" for Total Deaths. Insert "3" to exit. >>> ')
    if type[0] == "1":
        display_cases()

    elif type[0] == "2":
        display_deaths()
    
    elif type[0] == "3":
        running = False
        print("Exiting program.")
        exit

    else:
        print('Invalid input. Displaying Total Cases.')
        display_cases()
