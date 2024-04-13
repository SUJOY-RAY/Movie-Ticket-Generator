import mysql.connector
import streamlit as st
import pandas as pd

# Connect to database
def connect_to_database():
    return mysql.connector.connect(
        host="localhost",
        user="sujoyray",
        password="abcde",
        database="Movies"
    )

# Fetch data from database
def fetch_from_database(connection):
    query = "SELECT BookingID, Username, Age, Phno, MovieTitle, DATE_FORMAT(Showtime, '%Y-%m-%d %H:%i:%s'), SeatClass, NumberOfTickets, TicketPrice, BookingDate, TotalEarnings FROM TicketBookings"
    cursor=connection.cursor()
    cursor.execute(query)
    data=cursor.fetchall()
    cursor.close()
    return data


# Flush data from table
def delete_data(connection):
    query="Truncate TicketBookings"
    cursor=connection.cursor()
    cursor.execute(query)
    cursor.close()
    

def main():
    con=connect_to_database()

    st.title("Manager site")
    st.subheader("Information about the bookings")

    # Fetch data button    
    if st.button("Fetch data"):
        data=fetch_from_database(con)
        if len(data)==0:
            st.success("No data found ")
        else:
            df=pd.DataFrame(data, columns=["BookingID","Username","Age","Phno","MovieTitle","Showtime","SeatClass","NumberOfTickets","TicketPrice","BookingDate", "TotalEarnings"])
            st.table(df)
    
    # Flush data button
    if st.button("Flush Data"):
        delete_data(con)
        st.success("Data Flushed")
    con.close()

if __name__=="__main__":
    main()

            








