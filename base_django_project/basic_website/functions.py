import smtplib
from email.message import EmailMessage

def email_examp(my_mail, my_pass, contents, file=None):
        
        msg = EmailMessage()
        msg['Subject'] = contents['subject']
        msg['From'] = my_mail
        msg['To'] = my_mail
        msg.set_content(f"NAME: {contents['name']}\n\n \
             PHONE: {contents['phone']} \n\n \
             SENDER EMAIL: {contents['email_sender']}\n\n \
             MESSAGE: {contents['message']}\n\n")
        if file:
            with open(file, 'rb') as f:
                file_data = f.read()
                file_name = f.name
            msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as connection:
            connection.login(my_mail, my_pass)
            connection.send_message(msg)


file = None
if file:
    print('OKKK')

#email_examp(MY_EMAIL, MY_PASSWORD, contents)


"""
def email_requests(email_bussiness, subject, contents):
    mail_content = f"From: {contents['name']}\n\n Phone: {contents['phone']} \n\n \
        Mail: {contents['email_sender']} \n\n \
        Message: {contents['message']}"
    print(email_bussiness)
    print(MY_PASSWORD)
    print(subject)
    print(contents['name'])
    print(contents['phone'])
    print(contents['email_sender'])
    print(contents['message'])
    msg = EmailMessage()
    msg['From'] = email_bussiness
    msg['To'] = email_bussiness
    msg['Subject'] = subject
    msg.set_content(mail_content)
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.ehlo()
        connection.starttls()
        connection.login(MY_EMAIL,MY_PASSWORD)
        connection.sendmail(MY_EMAIL, MY_EMAIL, msg)



"""




