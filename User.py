import mysql.connector
import streamlit as st
import ticket_generator as tg

# Connect to MySQL
con = mysql.connector.connect(
    host="localhost",
    user="sujoyray",
    password="abcde",
    database="Movies"
)

def fetch_movie_list():
    cursor = con.cursor()
    cursor.execute("SELECT * FROM MovieList")  # Corrected table name
    movies = cursor.fetchall()
    return movies

def total_price(seat_class, num):
    price_list = {"First class": 500, "Second class": 400, "Third class": 250, "Fourth class": 150}
    return price_list[seat_class] * num

st.title("Book a Ticket")

# Personal Details
st.title("Personal Details")
username = st.sidebar.text_input("Enter your name")
Phno = st.sidebar.text_input("Enter your phone number")
age = st.sidebar.number_input("Enter your age", min_value=1, max_value=120)

# Movie selection
st.subheader("Select a Movie:")
movie_options = []
movies = fetch_movie_list()
for movie in movies:
    movie_options.append(movie[0])  # Assuming movie[0] contains the movie ID

MovieTitle = st.selectbox("Choose a movie", movie_options)

# Class of seats
SeatClass = st.selectbox("Class", ["First class", "Second class", "Third class", "Fourth class"])

# Number of tickets
st.subheader("Number of Tickets:")
NumberOfTickets = st.number_input("Enter the number of tickets", min_value=1, max_value=10, value=1)

# Calculate total price
TicketPrice = total_price(SeatClass, NumberOfTickets)

# Display total price
st.subheader("Total Cost:")
st.write(f"Rs. {TicketPrice}")

# Date selection
st.subheader("Select date:")
BookingDate = st.date_input("Choose a date")

# Time selection
st.subheader("Select Time:")
Showtime = st.time_input("Choose a time")

# Book button
if st.button("Book Now"):
    st.success("Tickets booked successfully!")
    tg.generate_ticket(username, Phno, MovieTitle, SeatClass, NumberOfTickets, Showtime, BookingDate)
    insert_query = "INSERT INTO TicketBookings (Username, Age, Phno, MovieTitle, Showtime, SeatClass, NumberOfTickets, TicketPrice, BookingDate) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
    cursor = con.cursor()
    cursor.execute(insert_query, (username, age, Phno, MovieTitle, Showtime, SeatClass, NumberOfTickets, TicketPrice, BookingDate))
    con.commit()
    con.close()
