import smtplib
import re
from email.mime.text import MIMEText

def sendEmail(sendTo):
    print(str(sendTo))
    if bool(re.match('^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', sendTo)):
        print(sendTo)
        sendFrom = "pythonTest0210@gmail.com"
        password = "pytest0210"
        
        smtp = smtplib.SMTP('smtp.gmail.com', 587)
        smtp.ehlo()
        smtp.starttls()
        smtp.login(sendFrom, password)

        try:
            msg = MIMEText('test')
            msg['Subject'] = "test"
            msg['To'] = sendTo
            smtp.sendmail(sendFrom, sendTo, msg.as_string())
        except Exception as e:
            print('error', e)
        finally:
            if smtp is not None:
                smtp.quit()
    else:
        print("enter the correct email")