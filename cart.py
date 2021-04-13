import mysql.connector
from tkinter import *
from tkinter import ttk

tk = Tk()
tk.geometry("1000x1000")

my_connect = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="PikuPiku1*",
  database="project"
)
entries=[]
windows=[]
def wait():
	
	my_conn.execute("DELETE FROM cart")
	my_connect.commit()
	for window in windows:
		window.destroy()
def conformation():
#payment.destroy()
	conformation_page=Tk()
	conformation_page.geometry("1000x1000")
	Label(conformation_page,text="Your order is confirmed and will be delivered", pady=10).pack()
	conn=my_connect.cursor()
	conn.execute("DELETE FROM cart")
	my_connect.commit()
	Button(conformation_page,text="OK",command=wait).pack()
	conformation_page.title("Conformation page")
	windows.append(conformation_page)
	conformation_page.mainloop()
def details():
 #payment.destroy()
	detail=Tk()
	detail.geometry("1000x1000")
	Label(detail,text="Enter the upi id or your card details",pady=10).grid()
	Label(detail,text="UPI ID").grid(row = 10,column=5)
	Label(detail,text="Card number").grid(row=15,column=5)
	Entry(detail).grid(row=10,column=9)
	Entry(detail).grid(row=15,column=9)
	Label(detail,text="cvv").grid(row=15,column=13)
	Entry(detail).grid(row=15,column=15)
	Button(detail,text="Confirm",command=conformation).grid(row=20,column=9)
	windows.append(detail)
	detail.title("Online Payment")
	detail.mainloop() 

def go_to():
	tk.destroy()
	payment=Tk()
	payment.geometry("1000x1000")
	w = Label(payment, text="Choose a method of payment",pady=10)
	w.pack()
	Button(payment,text="cash on delivery",command=conformation).pack(padx=5,pady=20)
	Button(payment,text="online payment",command=details).pack(padx=8,pady=25)
	payment.title("Payment page")
	windows.append(payment)
	payment.mainloop()
 
def submit():
	my_conn.execute("SELECT priceperunit FROM cart")
	s=0
	li=[]
	el=[]
	for i  in range(len(entries)):
		el.append(int(entries[i].get()) )
		print(int(entries[i].get()))
	for price in my_conn:
		li.append(int(float(price[0])) )
		print(int(float(price[0])))
	for n in range(len(entries)):
 		s=s+(el[n]*li[n]) 
	Label(tk,text='Final Price in Rupees',width=20).grid(row=i+6,column=5,pady=10)
	Label(tk,text=s,width=12).grid(row=i+6,column=6,pady=10)
	Button(tk,text='Payment',command=go_to).grid(row=i+10,column=6,pady=10)


my_conn = my_connect.cursor()
#my_conn.execute("SELECT NAME, BRAND, PRICEPERUNIT, QUANTITYPERUNIT from cart group by NAME having count(NAME)>1")
my_conn.execute("SELECT * from cart")


lb1= Label(tk,text='NAME', font=("Helvetica", 12)).grid(row=1,column=1,padx=10,pady=10)
lb1= Label(tk,text='BRAND', font=("Helvetica", 12)).grid(row=1,column=4,padx=10,pady=10)
lb1= Label(tk,text='PRICE PER UNIT', font=("Helvetica", 12)).grid(row=1,column=3,padx=10,pady=10)
lb1= Label(tk,text='QUANTITY PER UNIT\n(kg/litres/packs)', font=("Helvetica", 12)).grid(row=1,column=2,padx=10,pady=10)
lb1= Label(tk,text='NUMBER', font=("Helvetica", 12)).grid(row=1,column=5,padx=10,pady=10)

i=1
j=1
for item in my_conn:
	for j in range(len(item)):
		e = Entry(tk, width=10)
		e.grid(row=i+2, column=j+1,padx=10,pady=10) 
		e.insert(END, item[j])
		e.config(state='readonly')
	a = Entry(tk)
	a.grid(row=i+2,column=j+2,padx=10,pady=10)
	entries.append(a)
	i=i+1

Button(tk,text='Confirm',command=submit).grid(row=i+10,column=6,pady=10)
tk.title('Cart')
tk.mainloop()
