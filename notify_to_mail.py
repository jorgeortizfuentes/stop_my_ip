import smtplib

from config import email_password, email_receiver, email_sender


def sent_ip_to_email(
    message,
    subject,
    email_sender=email_sender,
    password=email_password,
    email_receiver=email_receiver,
):
    "Send a message to an email"
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email_sender, password)
    text_mail = f"Subject: {subject}\n\n{message}"
    server.sendmail(email_sender, email_receiver, text_mail)
    server.quit()
    return True
