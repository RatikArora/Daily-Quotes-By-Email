import smtplib
import random

connection = smtplib.SMTP_SSL('smtp.gmail.com', 465)
print("SMTP connection established ...")
file = open("quotes.txt",'r')
file = file.readlines()
quote = random.choice(file)
print("Selecting quote ...\n",quote)
mail = "Subject:QUOTE OF THE DAY \n\n"+quote

email = "everymondayquotes@gmail.com"
passw = "txgptkmnbalhtylm"

connection.login(user=email,password=passw)

# dt = datetime.now()
# x = dt.weekday()


def main(receiversmail) :
    print("Sending to : ",receiversmail)
    connection.sendmail(from_addr=email,to_addrs=receiversmail,msg=mail )

# connection.close()