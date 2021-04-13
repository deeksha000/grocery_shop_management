#nothing
#! /usr/bin/python

import mysql.connector
from testdr import *
mydb=mysql.connector.connect(host="localhost", user="root", password="PikuPiku1*", database="project")
from tkinter import *
import os
#from tkinter import ttk
from functools import partial
mycursor=mydb.cursor()

fp1 = open("groc_buttons.py","w")
fp1.close()
fp1 = open("groc_buttons.py","w")

print("I am chai")
#mycursor.execute("""INSERT INTO dummy (val1, val2) VALUES ('hello','Adios');""")
#mydb.commit()

mycursor.execute("select product_name from groceries")
groc=mycursor.fetchall()
fp1.write("import Query\n")
fp1.write("def groc_create(submenu,mycursor, top, mydb):\n")
for i in range(len(groc)):
	fp1.write("	submenu.add_command(label="+str(groc[i])+", command=lambda : Query.wait("+"\'groceries',"+str(i+1)+",mycursor, top, mydb))\n") 
	fp1.write("	submenu.add_separator()\n\n")

mycursor.execute("select product_name from milkproducts")
milkp=mycursor.fetchall()
fp1.write("def mp_create(submenu1,mycursor, top, mydb):\n")
for i in range(len(milkp)):
	fp1.write("	submenu1.add_command(label="+str(milkp[i])+", command=lambda : Query.wait("+"\'milkproducts',"+str(i+1)+",mycursor, top, mydb))\n") 
	fp1.write("	submenu1.add_separator()\n\n")

mycursor.execute("select product_name from fruits")
fruit=mycursor.fetchall()
fp1.write("def fruit_create(submenu2,mycursor, top, mydb):\n")
for i in range(len(fruit)):
	fp1.write("	submenu2.add_command(label="+str(fruit[i])+", command=lambda : Query.wait("+"\'fruits',"+str(i+1)+",mycursor, top, mydb))\n") 
	fp1.write("	submenu2.add_separator()\n\n")

mycursor.execute("select product_name from vegetables")
veggie=mycursor.fetchall()
fp1.write("def veggie_create(submenu3,mycursor, top, mydb):\n")
for i in range(len(veggie)):
	fp1.write("	submenu3.add_command(label="+str(veggie[i])+", command=lambda : Query.wait("+"\'vegetables',"+str(i+1)+",mycursor, top, mydb))\n") 
	fp1.write("	submenu3.add_separator()\n\n")

mycursor.execute("select product_name from healthcare")
hc=mycursor.fetchall()
fp1.write("def hc_create(submenu4,mycursor, top, mydb):\n")
for i in range(len(hc)):
	fp1.write("	submenu4.add_command(label="+str(hc[i])+", command=lambda : Query.wait("+"\'healthcare',"+str(i+1)+",mycursor, top, mydb))\n") 
	fp1.write("	submenu4.add_separator()\n\n")

fp1.close()




#def all_funcs():
	#g
	#openwindow()
        

#def openwindow():
#	if((flagp==1) and (flagl==1)):
#		top=Toplevel()
#		top.title("CATEGORIES")
#		top.geometry('400x400')
def register(tkWindow):
    tkWindow.destroy()
    registration_page()

def category(top):
	def wait(value):
		print("Just checkin")
		print(value)
		
	def logout():
		print("Logging out")  		#msg
		top.destroy()
	menu = Menu(top, background='lightblue', foreground='black')  	#creating a menu bar; background = color of menu bg obvio, foreground sets the color of box
	top.configure(menu = menu) 
	

	submenu=Menu(menu, background = 'white', foreground = 'black') 							#creating a submenu                       
	menu.add_cascade(label="GROCERIES", menu = submenu)
	#labeling the submenu
	#mycursor.execute("select product_name from groceries")
	#groc=mycursor.fetchall()
	#print(groc)									#debug 
	#print(len(groc))								#item 1
	#for i in range(len(groc)):
	#	submenu.add_command(label=groc[i], command=lambda : wait(5)) 
	#	submenu.add_separator()
	import groc_buttons
	groc_buttons.groc_create(submenu,mycursor, top, mydb)
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
	groc_buttons.mp_create(submenu1,mycursor, top, mydb)
	#mycursor.execute("select product_name from milkproducts")
	#milkp=mycursor.fetchall()
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
	groc_buttons.fruit_create(submenu2,mycursor, top, mydb)
	#mycursor.execute("select product_name from fruits")
	#fruit=mycursor.fetchall()
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
	groc_buttons.veggie_create(submenu3,mycursor, top, mydb)
	#mycursor.execute("select product_name from vegetables")
	#veggie=mycursor.fetchall()
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
	groc_buttons.hc_create(submenu4, mycursor, top, mydb)
	#mycursor.execute("select product_name from healthcare")
	#hc=mycursor.fetchall()
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
	
		
	

def validateLogin(loginid, password):
	
	flagp=0
	flagl=0
	pos=-1
	print("Login id entered:", loginid.get())
	login1 = loginid.get()
	print('login1', login1)
	os.system("rm -rf email_id.txt")
	fpm=open("email_id.txt", "w")
	fpm.write(login1)
	fpm.close()
	mycursor.execute("select id from customer")
	result=mycursor.fetchall()
	login = '(\''+loginid.get()+'\',)'
	print(login)
	for i in range(len(result)):
		#print(result[i])         #your debug point when you have to print db element
		if (login!=str(result[i])):
			flagl=0
		else:
                #print("valid loginid")
			flagl=1
			pos=i
			break
	if(flagl==1):
		print("valid loginid")
            #flag=0
	else:
		print("Invalid loginid")
	print("Password entered:", password.get())
	mycursor.execute("select password from customer")
	result1=mycursor.fetchall()
	#print(result1)
	passwrd = '(\''+password.get()+'\',)'
	print(passwrd)
	if (passwrd!=str(result1[pos])):
		flagp=0
	else:
		flagp=1
	if(flagp==1):
		print("valid password")
	else:
		print("invalid password")
	if((flagp==1) and (flagl==1)):
		print("login successful")
		label1 = Label(tkWindow, text = "\t\t\t").grid(row=15, column=2)
		suclabel = Label(tkWindow, text = "LOGGED IN SUCCESSFULLY").grid(row=15, column=2)
		tkWindow.destroy()
		top=Tk()
		top.title("CATEGORIES")
		top.geometry('500x400')
		top['bg']='white'
		category(top)
		#categlabel=Label(top, text = "GROCERIES").grid(row=10, column = 10)
		
		
	else:
		print("try again")
		label2 = Label(tkWindow, text = "\t\t\t").grid(row=15, column=2)
		errlabel = Label(tkWindow, text = "Oops! Try again").grid(row=15, column=2)
	
		
	return


tkWindow = Tk()
tkWindow.geometry('400x400')
tkWindow.title("Welcome")
#img = ImageTk.PhotoImage(file= "/home/karthik/dbms_proj/FE/background.jpeg")
#img = img.resize((450, 350), Image.ANTIALIAS)
#l1 = Label(tkWindow, image=img)
#l1.place(x=0, y=0, relwidth = 1, relheight = 1)
loginidLabel=Label(tkWindow, text="Login Id").grid(row=10, column = 1)
#loginidLabel.pack()
loginid=StringVar()
loginidEntry = Entry(tkWindow, textvariable=loginid).grid(row=10,column=2)
passwordLabel=Label(tkWindow, text = "Password").grid(row=11, column=1)
password=StringVar()
passwordEntry=Entry(tkWindow, textvariable=password, show = '*').grid(row=11, column=2)
g=partial(validateLogin,loginid, password)
loginButton = Button(tkWindow, text='Login', command=g).grid(row=12, column=2) 
registrationbutton=Button(tkWindow, text = 'Register', command =lambda : register(tkWindow)).grid(row=20, column = 2) 
tkWindow.mainloop()



