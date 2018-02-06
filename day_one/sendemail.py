import smtplib
import psycopg2

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("feedback@bmsit.in", "Feedback@01")

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
msg = "Dear "+data1[0][0]+"["+data1[0][2]+"],\n\nPlease give the faculty review for this semester using the link: http://feedback.bmsit.ac.in\n\nPowered by DevX"
server.sendmail("feedback@bmsit.in", "amoghsk279@gmail.com", msg)





server.quit()
