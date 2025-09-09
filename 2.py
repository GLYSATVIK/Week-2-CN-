import smtplib
import logging
from email.message import EmailMessage

def send_ethereal_email():
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s - %(levelname)s - %(message)s')


    smtp_server = "smtp.ethereal.email"
    smtp_port = 587
    sender_email = "myrtie53@ethereal.email"
    password = "w5cdUNEfZaCebRtTKG"
    recipient_email = input("Enter recipient email (can be any email): ").strip()

    msg = EmailMessage()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = "Test Email via Ethereal SMTP"
    msg.set_content("Hello,\n\nThis is a test email sent via Ethereal SMTP server.\n\nRegards,\nPython Script")

    try:
        logging.info("Connecting to Ethereal SMTP server...")
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.set_debuglevel(1)
        server.ehlo()
        server.starttls()
        server.ehlo()
        logging.info("Logging in...")
        server.login(sender_email, password)
        logging.info("Sending email...")
        server.send_message(msg)
        logging.info("Email sent successfully.")
        print("You can view this email at your Ethereal dashboard.")
    except Exception as e:
        logging.error(f"Error occurred: {e}")
    finally:
        server.quit()
        logging.info("SMTP connection closed.")

if __name__ == "__main__":
    send_ethereal_email()
