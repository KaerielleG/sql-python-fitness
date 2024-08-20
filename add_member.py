import mysql.connector
from mysql.connector import Error

def add_member(id, name, age):
    try:
        
        connection = mysql.connector.connect(
            host='localhost',         
            database='fitnesscenter_db',           
            user='root',              
            password='Home0415'  
        )
        if connection.is_connected():
            cursor = connection.cursor()

            # SQL query to insert a new member
            sql_query = """
            INSERT INTO Members (id, name, age)
            VALUES (%s, %s, %s)
            """
            
            # Execute the query with provided data
            cursor.execute(sql_query, (id, name, age))
            
            
            connection.commit()
            print("Member added successfully!")
    
    except Error as e:
       
        print(f"Error: {e}")
    
    finally:
       
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")


add_member(1, 'John Doe', 30)
