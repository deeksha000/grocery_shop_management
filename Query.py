from tkinter import * 
from project import *
l=[]
def wait(Category,prod_id,mycursor, top, mydb):
	def add_cart():
		lstt=[product_name,quantityperunit,priceperunit,brand]
		mycursor.execute("INSERT INTO cart VALUES ('" +lstt[0]+"','"+str(lstt[1])+"','"+str(lstt[2])+"','"+str(lstt[3])+"')")
		val = (product_name,quantityperunit,priceperunit, brand)
		mydb.commit()
		
	

	def go_cart():
		function_1(top)			
		
	
	if(Category == "vegetables" or Category == "fruits"):
		mycursor.execute("select product_name, quantityperunit, priceperunit from "+Category+" where product_id = "+str(prod_id))
	else:
		mycursor.execute("select product_name, brand, quantityperunit, priceperunit from "+Category+" where product_id = "+str(prod_id))
	query=mycursor.fetchall()
	print(prod_id)
	print(query[0][0])
	if(Category == "vegetables" or Category == "fruits"):
		product_name=query[0][0]
		brand='Go Green'
		quantityperunit=query[0][1]
		priceperunit=query[0][2]
	else:
		product_name=query[0][0]
		brand=query[0][1]
		quantityperunit=query[0][2]
		priceperunit=query[0][3]
		
	
	space="					"							
	loginidLabel101=Label(top, text= space+"\n"+space+"\n"+space+"\n"+space, foreground = 'blue', background='white') #.grid(row=100, column = 100)
	loginidLabel101.place(relx=.5, rely=.25, anchor="center")
	loginidLabel100=Label(top, text= "PRODUCT: "+product_name+"\n"+"BRAND: "+brand+"\n"+"QUANTITY PER UNIT: "+str(quantityperunit)+"\n"+"PRICE PER UNIT: Rs."+str(priceperunit), foreground = 'black', background='pink')   #.grid(row=100, column = 100)
	loginidLabel100.place(relx=.5, rely=.25, anchor="center")
	addtocartbutton=Button(top, text='Add to cart', command=add_cart, background='gray', foreground='white')
	addtocartbutton.place(relx=0.5, rely=.65, anchor="center")
	gotocartbutton=Button(top, text='Go to cart', command=go_cart, background='gray', foreground='white')
	gotocartbutton.place(relx=1, rely=.5, anchor="ne")
	
	#loginidLabel102=Label(top, text="                                          ", foreground = 'blue', background='white')#.grid(row=101, column = 100)
	#loginidLabel102.place(relx=.6, rely=.25, anchor="center")
	#loginidLabel101.place(x=25, y=25, anchor="center")
	#loginidLabel103=Label(top, text=brand, foreground = 'blue', background='white')   #.grid(row=101, column = 100)
	#loginidLabel103.place(relx=.6, rely=.25, anchor="center")
	#loginidLabel100.pack()
	
	#top1.destroy()
	#top1=Tk()
	#top1.geometry("300x300")
	#top1['bg']='lightblue'
