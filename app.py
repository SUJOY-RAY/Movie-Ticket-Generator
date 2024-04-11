import mysql.connector
import streamlit as st
from datetime import date,time
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

def book_tickets(movie_id, num_tickets, time):
    pass

def total_price(seat_class, num):
    price_list = {"First class": 500, "Second class": 400, "Third class": 250, "Fourth class": 150}
    return price_list[seat_class] * num

st.title("Book a Ticket")

# Personal Details
st.title("Personal Details")
name = st.sidebar.text_input("Enter your name")
age = st.sidebar.number_input("Enter your age", min_value=1, max_value=120)
phone_number = st.sidebar.text_input("Enter your phone number")






# Movie selection
st.subheader("Select a Movie:")
movie_options = []
movies = fetch_movie_list()
for movie in movies:
    movie_options.append(movie[0])  # Assuming movie[0] contains the movie ID

selected_movie = st.selectbox("Choose a movie", movie_options)

# Class of seats
seatClass = st.selectbox("Class", ["First class", "Second class", "Third class", "Fourth class"])

# Number of tickets
st.subheader("Number of Tickets:")
num_tickets = st.number_input("Enter the number of tickets", min_value=1, max_value=10, value=1)

# Calculate total price
total_cost = total_price(seatClass, num_tickets)

# Display total price
st.subheader("Total Cost:")
st.write(f"Rs. {total_cost}")

# Date selection
st.subheader("Select date:")
selected_date=st.date_input("Choose a date")

# Time selection

st.subheader("Select Time:")
selected_time = st.time_input("Choose a time")

# Book button
if st.button("Book Now"):
    movie_id = selected_movie
    book_tickets(movie_id, num_tickets, selected_time)
    st.success("Tickets booked successfully!")
    tg.generate_ticket(name,phone_number,selected_movie,seatClass,num_tickets,selected_time,selected_date)
