import smtplib
import send_email_config.py

content = "example email stuff here"

mail = smtplib.SMTP('smtp.gmail.com', 587)

mail.ehlo()  # identifying ourself to server

mail.starttls()  # anything after this is encrypted

from_user = send_email_config.from_user
to = send_email_config.to
password = send_email_config.password

mail.login(from_user, password)  # to login, if your gmail has 2 step verification, you would need to generate a new
# password for this app

mail.sendmail(from_user, to, content)

mail.close()
