from project import * 
import tkinter as tk 
import mysql.connector
my_connect=mysql.connector.connect(host="localhost", user="root", password="PikuPiku1*", database="project")
#from tkinter import ttk
from functools import partial
my_conn=my_connect.cursor()
def registration_page():	
	root=tk.Tk() 
	def cat(tk):
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
			#submenu2.add_command(label="Milk", command = lambda : wai
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
	# setting the windows size 
	root.geometry("600x400")
	root['bg']='white' 
	   
	# declaring string variable 
	# for storing name and password 
	gmail = tk.StringVar()
	address=tk.StringVar()
	name_var=tk.StringVar() 
	passw_var=tk.StringVar() 
	  
	   
	# defining a function that will 
	# get the name and password and  
	# print them on the screen 
	def submit(): 
	    gmail_id = gmail.get()
	    name=name_entry.get() 
	    password=passw_var.get() 
	    add= address.get()
	      
	    print("The name is : " + name) 
	    print("The password is : " + password) 
	    print(add)
	    print(gmail_id)
	    address.set("") 
	    gmail.set("")     
	    name_var.set("") 
	    passw_var.set("")     
	    lstt=[gmail_id,name,password,add]
	    my_conn.execute("INSERT INTO customer VALUES ('" +lstt[0]+"','"+str(lstt[1])+"','"+str(lstt[2])+"','"+str(lstt[3])+"')")
	    val = (gmail_id,name,password,address)
	    my_connect.commit()
	    cat(root)
	    
	# name using widget Label 
	gmail_label = tk.Label(root, text = 'gmail_id', 
		              font=('calibre', 
		                    10, 'bold')) 
	   
	# creating a entry for input 
	# name using widget Entry 
	gmail_entry = tk.Entry(root, 
		              textvariable = gmail, 
		              font=('calibre',10,'normal')) 
		              
	   
	# creating a label for 
	# name using widget Label 
	address_label = tk.Label(root, text = 'Address', 
		              font=('calibre', 
		                    10, 'bold')) 
	   
	# creating a entry for input 
	# name using widget Entry 
	address_entry = tk.Entry(root, 
		              textvariable = address, 
		              font=('calibre',10,'normal')) 
	    
	# name using widget Label 
	name_label = tk.Label(root, text = 'Name', 
		              font=('calibre', 
		                    10, 'bold')) 
	   
	# creating a entry for input 
	# name using widget Entry 
	name_entry = tk.Entry(root, 
		              textvariable = name_var, 
		              font=('calibre',10,'normal')) 
	   
	# creating a label for password 
	passw_label = tk.Label(root, 
		               text = 'Password', 
		               font = ('calibre',10,'bold')) 
	   
	# creating a entry for password 
	passw_entry=tk.Entry(root, 
		             textvariable = passw_var, 
		             font = ('calibre',10,'normal'), 
		             show = '*') 
	   
	# creating a button using the widget  
	# Button that will call the submit function  
	sub_btn=tk.Button(root,text = 'Submit', 
		          command = submit) 
	   
	# placing the label and entry in 
	# the required position using grid 
	# method 
	name_label.grid(row=0,column=0) 
	name_entry.grid(row=0,column=1) 
	passw_label.grid(row=1,column=0) 
	passw_entry.grid(row=1,column=1) 
	gmail_entry.grid(row=2,column=1)
	gmail_label.grid(row=2,column=0)
	address_entry.grid(row=3,column=1)
	address_label.grid(row=3,column=0)
	sub_btn.grid(row=6,column=1) 
	   
	# performing an infinite loop  
	# for the window to display 
	root.mainloop() 
