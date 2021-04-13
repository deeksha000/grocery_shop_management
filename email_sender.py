import os
import smtplib 
 
from email.message import EmailMessage 
#EMAIL_MESSAGE = os.environ.get('EMAIL_USER')

def send_email():
	with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
		print("Sending Email.......")
		fpt = open("email_id.txt",'r')
		customer_email = fpt.readline()
		customer_email = customer_email.strip('\n')
		fpt.close()
		
		smtp.ehlo()
		smtp.starttls()
		smtp.ehlo()
		smtp.login('teamcdminiproj@gmail.com', 'dbmsmini')
		subject = 'order confirmation'
		body = 'Dear Customer,\n\nYour order has been placed and your package will be shipped soon!!!\n\nRegards,\nCD Team'
		msg = f'Subject: {subject}\n\n{body}'
		smtp.sendmail('teamcdminiproj@gmail.com', customer_email, msg)
