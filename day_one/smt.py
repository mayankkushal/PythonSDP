import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import psycopg2

conn = psycopg2.connect(database='feedback', user='feedback', password='feedback123', host='128.199.250.218', port='5432')
cursor = conn.cursor()

cursor.execute("""SELECT distinct b.first_name, b.email, b.username
               FROM public.main_userprofile a, public.auth_user b
               WHERE a.done = false AND a.id = b.id AND a.mtech = 'true'""")
data1 = cursor.fetchall()

cursor.execute("""SELECT distinct b.first_name, b.email, b.username
               FROM public.main_userprofile a, public.auth_user b
               WHERE a.done = false AND a.id = b.id AND a.dno_id = 8""")
data2 = cursor.fetchall()


fromaddr = "feedback@bmsit.in"
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['Subject'] = "Faculty feedback"
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, "Feedback@01")


for i in data1:
    msg['To'] = str(i[1])
    body = "Dear " + i[0] + " [" + i[2] + "],\n\nPlease give the faculty review for this semester using the link: http://feedback.bmsit.ac.in\n\nPowered by DevX"
    msg.attach(MIMEText(body, 'plain'))
    text = msg.as_string()
    server.sendmail(fromaddr, i[1], body)
    print("Message sent to %s [%s] Email: %s" % (i[0], i[2], i[1]))

for i in data2:
    msg['To'] = str(i[1])
    body = "Dear " + i[0] + " [" + i[2] + "],\n\nPlease give the faculty review for this semester using the link: http://feedback.bmsit.ac.in\n\nPowered by DevX"
    msg.attach(MIMEText(body, 'plain'))
    text = msg.as_string()
    server.sendmail(fromaddr, i[1], body)
    print("Message sent to %s[%s] Email: %s" % (i[0], i[2], i[1]))


server.quit()
