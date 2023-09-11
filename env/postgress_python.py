import psycopg2

# Database connection parameters
hostname = "localhost"
database_name = "scripting"
username = "postgres"
password = "djangohero"
port = 5432

try:
    # Establish a connection to the PostgreSQL database
    connection = psycopg2.connect(
        host = hostname,
        database = database_name,
        user = username,
        password = password,
        port = port
        
    )
    
    cur = connection.cursor()
    connection.commit()
    
    create_script = '''create table if not exists employee(
            id  int primary key,
            name varchar(40) not null,
            dept_id varchar(30))'''

    cur.execute(create_script)
    
    
    
    



   
    

except psycopg2.Error as error:
    print("Error connecting to the database:", error)

finally:
        if cur is not None:
            cur.close()
        if connection is not None:        
            connection.close()
