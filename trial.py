import mysql.connector

# Establish a connection to the MySQL server
connection = mysql.connector.connect(
    host="localhost",
    user="sujoyray",
    password="abcde",
    database="Movies"
)

if connection.is_connected():
    print("Connected to MySQL server")
def AddMovieRec(Movie_ID, Movie_Name, Release_Date, Director, Cast, Budget, Duration, Rating):
    # Connect to MySQL
    con = mysql.connector.connect(
        host="localhost",
        user="sujoyray",
        password="abcde",
        database="MovieDB"
    )
    cur = con.cursor()

    # Insert the movie record
    cur.execute("INSERT INTO movie (Movie_ID, Movie_Name, Release_Date, Director, Cast, Budget, Duration, Rating) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", (Movie_ID, Movie_Name, Release_Date, Director, Cast, Budget, Duration, Rating))
    
    con.commit()
    con.close()

def ViewMovieData():
    # Connect to MySQL
    con = mysql.connector.connect(
        host="localhost",
        user="your_username",
        password="your_password",
        database="your_database"
    )
    cur = con.cursor()

    # Retrieve all movie records
    cur.execute("SELECT * FROM movie")
    rows = cur.fetchall()
    
    con.close()
    
    return rows
print("end")
