import smtplib
import re
from email.mime.text import MIMEText
import random 

def sendEmail(sendTo):
    global correct_email,cert_num
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


def sendEmail_find_id(email,id_list):

    if bool(re.match('^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email)):
        print(email)
        sendFrom = "pythonTest0210@gmail.com"
        password = "pytest0210"
        
        smtp = smtplib.SMTP('smtp.gmail.com', 587)
        smtp.ehlo()
        smtp.starttls()
        smtp.login(sendFrom, password)
        try:
            sen = '{}로 가입된 ID는 \n\n'.format(email)
            for i in id_list:
                # if i==id_list[-1]:
                #     sen+=i+
                # else:
                #     sen+=i+"\n"
                sen+=i+'\n\n'
            sen+="입니다."
            msg = MIMEText(sen)
            msg['Subject'] = "ID 발송"
            msg['To'] = email
            smtp.sendmail(sendFrom, email, msg.as_string())
        except Exception as e:
            print('error', e)
        finally:
            if smtp is not None:
                smtp.quit()
    else:
        print("enter the correct email")