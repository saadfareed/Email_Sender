import smtplib, ssl
port = 465  # For SSL
password = input("Type your password and press enter: ")
SenderAddress="fareedmsaad@gmail.com"
# Create a secure SSL context
context = ssl.create_default_context()
email="saadfareed632@gmail.com,saadfareed282681@gmail.com"
email=email.split(",")
print(email)
print(type(email))
msg = "Hello this is a email form Saad Fareed let's have a fun buddy."
subject = "Hello world"
body = "Subject: {}\n\n{}".format(subject,msg)
with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login("fareedmsaad@gmail.com", password)
    # TODO: Send email here
    server.sendmail(SenderAddress,email,body)
    server.quit()
