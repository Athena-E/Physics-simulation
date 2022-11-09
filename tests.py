# # Import smtplib for the actual sending function
# import smtplib

# # Import the email modules we'll need
# from email.message import EmailMessage

# textfile = "emailmsg.txt"

# # Open the plain text file whose name is in textfile for reading.
# with open(textfile) as fp:
#     # Create a text/plain message
#     msg = EmailMessage()
#     msg.set_content(fp.read())

# # me == the sender's email address
# # you == the recipient's email address
# msg['Subject'] = f'The contents of {textfile}'
# msg['From'] = "athena.eng2004@gmail.com"
# msg['To'] = "p216072@prioryacademies.co.uk"

# # Send the message via our own SMTP server.
# s = smtplib.SMTP('localhost')
# s.send_message(msg)
# s.quit()

# import os

# API_URL = "https://vzvimxkzvvjyohbeodlq.supabase.co"
# API_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InZ6dmlteGt6dnZqeW9oYmVvZGxxIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTY2MjI3NzEwNiwiZXhwIjoxOTc3ODUzMTA2fQ.vIPGMLpxL5Gnv5aLrI4_1CJvCGq3-aO-BPu9ll_s3gU"

# with open(".env", "w") as f:
#     f.write("API_URL=https://vzvimxkzvvjyohbeodlq.supabase.co")
#     f.write("API_KEY=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InZ6dmlteGt6dnZqeW9oYmVvZGxxIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTY2MjI3NzEwNiwiZXhwIjoxOTc3ODUzMTA2fQ.vIPGMLpxL5Gnv5aLrI4_1CJvCGq3-aO-BPu9ll_s3gU")

# print("done")


print(False==None)


