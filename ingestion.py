from pybaseball import statcast, cache
import pandas as pd
import os
import sqlite3

DATA_FILE="project/data.csv"
DB_FILE=r"data/data.db"

def main():
    cache.enable()
    current_folder = os.path.dirname(__file__)
    db_path = os.path.join(current_folder, DB_FILE)
    if not os.path.exists(os.path.dirname(db_path)):
        os.makedirs(os.path.dirname(db_path))
    db = connect_to_db(db_path)
    data = statcast(start_dt='2022-06-01', end_dt='2022-06-30')
    data.to_sql("statcast", db, if_exists="fail")

def connect_to_db(db_file: str) -> sqlite3.Connection:
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except sqlite3.Error as e:
        print(e)

    return conn

if __name__ == "__main__":
    main()