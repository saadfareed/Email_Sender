import pandas as pd
import smtplib, ssl
port = 465  # For SSL
password = input("Type your password and press enter: ")
SenderAddress="fareedmsaad@gmail.com"
context = ssl.create_default_context()
email="talha17102000@gmail.com"
data = pd.read_csv (r'email.csv') 
email_list = data["email"].tolist() 
#print(type(email_list))
for i in email_list:
    msg = "Hello this is a email form Saad Fareed let's have a fun buddy."
    subject = "Hello world"
    body = "Subject: {}\n\n{}".format(subject,msg)
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login("fareedmsaad@gmail.com", password)
        # TODO: Send email here
        print("wait it's sending............")
        print(" ")
        server.sendmail(SenderAddress,email,body)
        server.quit()
