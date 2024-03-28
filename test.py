import psycopg2
conn = psycopg2.connect(database = "utkarshshrivastava", 
                        user = "postgres", 
                        host= 'localhost',
                        password = "qwerty121!",
                        port = 5432)

# Open a cursor to perform database operations
cur = conn.cursor()
# Execute a command: create datacamp_courses table
cur.execute("""CREATE TABLE student(
            student_id SERIAL PRIMARY KEY,
            student_name VARCHAR (50) UNIQUE NOT NULL,
            """)
# Make the changes to the database persistent
conn.commit()
# Close cursor and communication with the database
cur.close()
conn.close()

