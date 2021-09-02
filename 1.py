import pandas as pd
import smtplib, ssl
port = 465  # For SSL
password = input("Type your password and press enter: ")
SenderAddress="fareedmsaad@gmail.com"
# Create a secure SSL context
#df = pd.read_csv('email.csv')
#df=df.values
#print(type(df))
#print(df)
context = ssl.create_default_context()
email="talha17102000@gmail.com"
email=email.split(",")
#print(email)
inu=3
#print(type(email))
msg = "Hello this is a email form Saad Fareed let's have a fun buddy."
subject = "Hello world"
body = "Subject: {}\n\n{}".format(subject,msg)
with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login("fareedmsaad@gmail.com", password)
    # TODO: Send email here
    while inu>1:
        server.sendmail(SenderAddress,email,body)
        inu=inu-1
        print(inu)
    server.quit()
