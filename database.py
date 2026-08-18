import sqlite3
import pandas as pd


DATABASE = "financial_data.db"


def execute_query(sql):

    connection = sqlite3.connect(DATABASE)

    try:
        dataframe = pd.read_sql_query(sql, connection)
        return dataframe

    finally:
        connection.close()