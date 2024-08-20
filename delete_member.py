import mysql.connector
from mysql.connector import Error

def delete_workout_session(session_id):
    try:
        
        connection = mysql.connector.connect(
            host='localhost',         
            database='fitness_db',          
            user='root',              
            password='Home0415'  
        )
        
        if connection.is_connected():
            cursor = connection.cursor()
            
            
            cursor.execute("SELECT * FROM WorkoutSessions WHERE session_id = %s", (session_id,))
            session = cursor.fetchone()
            
            if session:
                # SQL query to delete the workout session
                delete_query = "DELETE FROM WorkoutSessions WHERE session_id = %s"
                cursor.execute(delete_query, (session_id,))
                
               
                connection.commit()
                print("Workout session deleted successfully!")
            else:
                print(f"Workout session with ID {session_id} does not exist.")
    
    except Error as e:
        print(f"Error: {e}")
    
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

delete_workout_session(101)
