from fpdf import FPDF
import qrcode

# Function to generate PDF ticket
def generate_ticket(name, phone_no, movie_title, seat_class, num_tickets, time, date):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12, style="B")

    # BG Image
    pdf.image("/home/arclight/Coding/DBMS Projects/Movie-Watchlist-using-python/img.jpg", x=0, y=0, w=210, h=297, )

    # Title
    pdf.set_fill_color(200, 220, 255)  # Light blue background color
    pdf.cell(200, 10, txt="Ticket Information", ln=True, align="C", fill=True, border=0)  # No border
    pdf.cell(200, 10, ln=True)

    # Movie title
    pdf.set_fill_color(255, 255, 255)  # White background color
    pdf.cell(200, 10, txt=f"Movie: {movie_title}", ln=True, border=0)  # No border

    # Name
    pdf.cell(200, 10, txt=f"Name: {name}", ln=True, border=0)  # No border

    # Phone No
    pdf.cell(200, 10, txt=f"Phone number: {phone_no}", ln=True, border=0)  # No border

    # Seat class
    pdf.cell(200, 10, txt=f"Seat Class: {seat_class}", ln=True, border=0)  # No border

    # Number of tickets
    pdf.cell(200, 10, txt=f"Number of Tickets: {num_tickets}", ln=True, border=0)  # No border

    # Time
    pdf.cell(200, 10, txt=f"Time: {time}", ln=True, border=0)  # No border
    pdf.cell(200, 10, txt=f"Date: {date}", ln=True, border=0)  # No border

    # Generate QR code
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
    qr.add_data(f"Name: {name}\nPhone number: {phone_no}\nMovie: {movie_title}\nSeat Class: {seat_class}\nNumber of Tickets: {num_tickets}\nTime: {time}\nDate: {date}")
    qr.make(fit=True)

    # Save QR code as image
    qr_img = qr.make_image(fill_color="black", back_color="white")
    qr_img.save("qrcode.png")

    # Add QR code to PDF
    pdf.image("qrcode.png", x=10, y=150, w=40, h=40)

    pdf.output("ticket_with_qr.pdf")


