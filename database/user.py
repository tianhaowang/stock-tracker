import database.connect as db

from werkzeug.security import check_password_hash

def login(username, provided_password):
    connection = db.get_database_connection()
    cursor = connection.cursor()

    select_query = f"SELECT username, password FROM users WHERE username = %s"
    
    try:
        cursor.execute(select_query, (username,))  # Use parameters to prevent SQL injection
        result = cursor.fetchone()  # fetchone since usernames are unique
        if result:
            stored_password = result[1]  # Assuming the second column is the password
            if check_password_hash(stored_password, provided_password):
                return result  # User authenticated successfully
            else:
                return None  # Incorrect password
        else:
            return None  # User not found
        
    except Exception as e:
        print(f"Error while retrieving user record: {e}")
        return None
    finally:
        cursor.close()
        connection.close()