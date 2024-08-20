
import mysql.connector 
from mysql.connector import Error

#Database connection parementers 
db_name ='fitness_db'
user = "root"
password = "Home0415"
host = "localhost"

try: 
    conn = mysql.connector.connect(
        database = db_name,
        user = user, 
        password = password,
        host = host
    )
    
    if conn.is_connected():
        print("Connected to MySQL database successfully")

except Error as e: 
    print(f"Error: {e}")

finally: 
    if conn and conn.is_connected():
        conn.close()
        print("MySQL connection is closed.")
