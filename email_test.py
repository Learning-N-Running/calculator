import smtplib
import re
from email.mime.text import MIMEText
import random 

def sendEmail(sendTo):
    global correct_email
    correct_email = True
    if bool(re.match('^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', sendTo)):
        print(sendTo)
        sendFrom = "pythonTest0210@gmail.com"
        password = "pytest0210"
        
        smtp = smtplib.SMTP('smtp.gmail.com', 587)
        smtp.ehlo()
        smtp.starttls()
        smtp.login(sendFrom, password)

        try:
            cert_num = random.randrange(1000,10000)
            msg = MIMEText('인증 번호는 {}입니다'.format(cert_num))
            msg['Subject'] = "인증번호 발송"
            msg['To'] = sendTo
            smtp.sendmail(sendFrom, sendTo, msg.as_string())
        except Exception as e:
            print('error', e)
        finally:
            if smtp is not None:
                smtp.quit()
    else:
        print("enter the correct email")
        correct_email = False