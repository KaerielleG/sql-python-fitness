import mysql.connector
from mysql.connector import Error

def update_member_age(member_id, new_age):
    try:
      
        connection = mysql.connector.connect(
            host='localhost',        
            database='fitness_db',         
            user='root',              
            password='Home0415'  
        )
        
        if connection.is_connected():
            cursor = connection.cursor()
            
           
            cursor.execute("SELECT * FROM Members WHERE id = %s", (member_id,))
            member = cursor.fetchone()
            
            if member:
               
                update_query = """
                UPDATE Members
                SET age = %s
                WHERE id = %s
                """
                cursor.execute(update_query, (new_age, member_id))
                
               
                connection.commit()
                print("Member's age updated successfully!")
            else:
                print(f"Member with ID {member_id} does not exist.")
    
    except Error as e:
        print(f"Error: {e}")
    
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

