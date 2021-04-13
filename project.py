import mysql.connector
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import email_sender


def function_1(category):
	category.destroy()
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
	 email_sender.send_email()
	 for window in windows:
	  window.destroy()
	def conformation():
	 #payment.destroy()
	 conformation_page=Tk()
	 conformation_page.geometry("1000x1000")
	 Label(conformation_page,text="Your order is confirmed and will be delivered", pady=10).pack()
	 conn=my_connect.cursor()
	 conn.execute("DELETE FROM cart")
	 Button(conformation_page,text="OK",command=wait).pack()
	 conformation_page.title("Conformation page")
	 windows.append(conformation_page)
	 conformation_page.mainloop()

	def cat_1(tk):
	 tk.destroy()
	 top = Tk()
	 top.geometry('500x400')
	 top.title("Categories")
	 top['bg']='white'
	 def wait(value):
	  print("Just checkin")
	  print(value)
			
	 def logout():
	  print("Logging out")  		#msg
	  top.destroy()
	 menu = Menu(top, background='lightblue', foreground='black') 
	 top.configure(menu = menu) 
		

	 submenu=Menu(menu, background = 'white', foreground = 'black') 							#creating a submenu                       
	 menu.add_cascade(label="GROCERIES", menu = submenu)
		#labeling the submenu
		#my_conn.execute("select product_name from groceries")
		#groc=my_conn.fetchall()
		#print(groc)									#debug 
		#print(len(groc))								#item 1
		#for i in range(len(groc)):
		#	submenu.add_command(label=groc[i], command=lambda : wait(5)) 
		#	submenu.add_separator()
	 import groc_buttons
	 groc_buttons.groc_create(submenu,my_conn, top,my_connect)
		#print("Val in main= "+str(val))
		#include("groc_buttons.py")
		#submenu.add_command(label="Sugar", command = lambda : wait(5))  			 
		#submenu.add_separator()
		#submenu.add_command(label="Salt", command = lambda : wait(5)) 
		#submenu.add_separator()
		#submenu.add_command(label="Wheat", command = lambda : wait(5)) 
		#submenu.add_separator()
		#submenu.add_command(label="Rice", command = lambda : wait(5)) 
		#submenu.add_separator()
		#submenu.add_command(label="Chilli Powder", command = lambda : wait(5)) 

	 submenu1=Menu(menu, background = 'white', foreground = 'black') 	#second submenu
	 menu.add_cascade(label="MILK PRODUCTS", menu = submenu1)
		#import groc_buttons
	 groc_buttons.mp_create(submenu1,my_conn, top,my_connect)
		#my_conn.execute("select product_name from milkproducts")
		#milkp=my_conn.fetchall()
		#print(milkp)
		#for i in range(len(milkp)):
		#	submenu2.add_command(label=milkp[i], command=lambda : wait(i)) 		
		#	print(i)
		#	submenu2.add_separator()
		#submenu2.add_command(label="Milk", command = lambda : wait(5)) 
		#submenu2.add_separator()
		#submenu2.add_command(label="Cheese", command = lambda : wait(5)) 
		#submenu2.add_separator()
		#submenu2.add_command(label="Paneer", command = lambda : wait(5)) 
		#submenu2.add_separator()
		#submenu2.add_command(label="Milk Powder", command = lambda : wait(5)) 
		#submenu2.add_separator()
		#submenu2.add_command(label="Curd", command = lambda : wait(5)) 	

	 submenu2=Menu(menu, background = 'white', foreground = 'black')         #third submenu
	 menu.add_cascade(label="FRUITS", menu = submenu2)
	 groc_buttons.fruit_create(submenu2,my_conn, top,my_connect)
		#my_conn.execute("select product_name from fruits")
		#fruit=my_conn.fetchall()
		#print(fruit)								#debug = db ;)
		#for i in range(len(fruit)):
		#	submenu3.add_command(label=fruit[i], command=lambda : wait(5)) 
		#	submenu3.add_separator()
		
		#submenu3.add_command(label="Mango", command = lambda : wait(5)) 
		#submenu3.add_separator()
		#submenu3.add_command(label="Grapes", command = lambda : wait(5)) 
		#submenu3.add_separator()
		#submenu3.add_command(label="Apple", command = lambda : wait(5)) 
		#submenu3.add_separator()
		#submenu3.add_command(label="Pineapple", command = lambda : wait(5)) 
		#submenu3.add_separator()
		#submenu3.add_command(label="Lichi", command = lambda : wait(5)) 

	 submenu3=Menu(menu, background = 'white', foreground = 'black')         #fourth submenu
	 menu.add_cascade(label="VEGETABLES", menu = submenu3)
	 groc_buttons.veggie_create(submenu3,my_conn, top, my_connect)
		#my_conn.execute("select product_name from vegetables")
		#veggie=my_conn.fetchall()
		#print(veggie)								#debug = db ;)
		#for i in range(len(veggie)):
		#	submenu4.add_command(label=veggie[i], command=lambda : wait(5)) 
		#	submenu4.add_separator()
		#submenu4.add_command(label="Carrot", command = lambda : wait(5)) 
		#submenu4.add_separator()
		#submenu4.add_command(label="Raddish", command = lambda : wait(5)) 
		#submenu4.add_separator()
		#submenu4.add_command(label="Potato", command = lambda : wait(5)) 
		#submenu4.add_separator()
		#submenu4.add_command(label="Onion", command = lambda : wait(5)) 
		#submenu4.add_separator()
		#submenu4.add_command(label="Pumpkin", command = lambda : wait(5)) 

	 submenu4=Menu(menu, background = 'white', foreground = 'black')         #fifth submenu
	 menu.add_cascade(label="HEALTH CARE", menu = submenu4)
	 groc_buttons.hc_create(submenu4, my_conn, top, my_connect)
		#my_conn.execute("select product_name from healthcare")
		#hc=my_conn.fetchall()
		#print(hc)								#db 
		#for i in range(len(hc)):
		#	submenu5.add_command(label=hc[i], command=lambda : wait(5)) 
		#	submenu5.add_separator()
		#submenu5.add_command(label="Mask", command = lambda : wait(5)) 
		#submenu5.add_separator()
		#submenu5.add_command(label="Sanitiser", command = lambda : wait(5)) 
		#submenu5.add_separator()



		#submenu5.add_command(label="Disinfectant", command = lambda : wait(5)) 
		#submenu5.add_separator()
		#submenu5.add_command(label="Face shield", command = lambda : wait(5)) 
		#submenu5.add_separator()
		#submenu5.add_command(label="Gloves", command = lambda : wait(5)) 	

	 logoutbutton=Button(top, text='Logout', command=logout, background='gray', foreground='white')
	 logoutbutton.place(relx=1, rely=0.0, anchor="ne")	
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
	  #print(type(int(entries[i].get())))
	 for price in my_conn:
	  li.append(int(float(price[0])) )
	  #print(type(int(float(price[0]))))
	 for n in range(len(entries)):
	  s=s+(el[n]*li[n]) 
	 Label(tk,text='Final Price in Rupees',width=20).grid(row=i+6,column=5,pady=10)
	 Label(tk,text=s,width=12).grid(row=i+6,column=6,pady=10)
	 Button(tk,text='Payment',command=go_to).grid(row=i+10,column=6,pady=10)


	my_conn = my_connect.cursor()
	my_conn.execute("SELECT DISTINCT * FROM cart")
	lb1= Label(tk,text='NAME',fg='white', font=("Helvetica", 12)).grid(row=1,column=1,padx=10,pady=10)
	lb1= Label(tk,text='BRAND',fg='white', font=("Helvetica", 12)).grid(row=1,column=4,padx=10,pady=10)
	lb1= Label(tk,text='PRICE PER UNIT',fg='white', font=("Helvetica", 12)).grid(row=1,column=3,padx=10,pady=10)
	lb1= Label(tk,text='QUANTITY PER UNIT',fg='white', font=("Helvetica", 12)).grid(row=1,column=2,padx=10,pady=10)
	lb1= Label(tk,text='NUMBER',fg='white', font=("Helvetica", 12)).grid(row=1,column=5,padx=10,pady=10)
	i=1
	j=1
	for item in my_conn:
	 for j in range(len(item)):
	  e = Entry(tk, width=10, fg='black')
	  e.grid(row=i+2, column=j+1,padx=10,pady=10) 
	  e.insert(END, item[j])
	  e.config(state='readonly')
	 a = Entry(tk)
	 a.grid(row=i+2,column=j+2,padx=10,pady=10)
	 entries.append(a)
	 i=i+1
	bt0=Button(tk,text='Confirm',command=submit).grid(row=i+10,column=6,pady=10)
	bt1=Button(tk,text='Back to cart',command=lambda: cat_1(tk)).grid(row=i+15,column=6,pady=10)
	tk.title('Cart')
	tk.mainloop()
		
		
		
		
		
