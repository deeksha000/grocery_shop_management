import Query
def groc_create(submenu,mycursor, top, mydb):
	submenu.add_command(label=('salt',), command=lambda : Query.wait('groceries',1,mycursor, top, mydb))
	submenu.add_separator()

	submenu.add_command(label=('sugar',), command=lambda : Query.wait('groceries',2,mycursor, top, mydb))
	submenu.add_separator()

	submenu.add_command(label=('Wheat',), command=lambda : Query.wait('groceries',3,mycursor, top, mydb))
	submenu.add_separator()

	submenu.add_command(label=('Rice',), command=lambda : Query.wait('groceries',4,mycursor, top, mydb))
	submenu.add_separator()

	submenu.add_command(label=('Chilli',), command=lambda : Query.wait('groceries',5,mycursor, top, mydb))
	submenu.add_separator()

def mp_create(submenu1,mycursor, top, mydb):
	submenu1.add_command(label=('Milk',), command=lambda : Query.wait('milkproducts',1,mycursor, top, mydb))
	submenu1.add_separator()

	submenu1.add_command(label=('Cheese',), command=lambda : Query.wait('milkproducts',2,mycursor, top, mydb))
	submenu1.add_separator()

	submenu1.add_command(label=('Paneer',), command=lambda : Query.wait('milkproducts',3,mycursor, top, mydb))
	submenu1.add_separator()

	submenu1.add_command(label=('MilkPowder',), command=lambda : Query.wait('milkproducts',4,mycursor, top, mydb))
	submenu1.add_separator()

	submenu1.add_command(label=('Curd',), command=lambda : Query.wait('milkproducts',5,mycursor, top, mydb))
	submenu1.add_separator()

def fruit_create(submenu2,mycursor, top, mydb):
	submenu2.add_command(label=('Mango',), command=lambda : Query.wait('fruits',1,mycursor, top, mydb))
	submenu2.add_separator()

	submenu2.add_command(label=('Grapes',), command=lambda : Query.wait('fruits',2,mycursor, top, mydb))
	submenu2.add_separator()

	submenu2.add_command(label=('Apple',), command=lambda : Query.wait('fruits',3,mycursor, top, mydb))
	submenu2.add_separator()

	submenu2.add_command(label=('Pineapple',), command=lambda : Query.wait('fruits',4,mycursor, top, mydb))
	submenu2.add_separator()

	submenu2.add_command(label=('Lichi',), command=lambda : Query.wait('fruits',5,mycursor, top, mydb))
	submenu2.add_separator()

def veggie_create(submenu3,mycursor, top, mydb):
	submenu3.add_command(label=('Carrot',), command=lambda : Query.wait('vegetables',1,mycursor, top, mydb))
	submenu3.add_separator()

	submenu3.add_command(label=('Raddish',), command=lambda : Query.wait('vegetables',2,mycursor, top, mydb))
	submenu3.add_separator()

	submenu3.add_command(label=('Potato',), command=lambda : Query.wait('vegetables',3,mycursor, top, mydb))
	submenu3.add_separator()

	submenu3.add_command(label=('Onion',), command=lambda : Query.wait('vegetables',4,mycursor, top, mydb))
	submenu3.add_separator()

	submenu3.add_command(label=('Pumpkin',), command=lambda : Query.wait('vegetables',5,mycursor, top, mydb))
	submenu3.add_separator()

def hc_create(submenu4,mycursor, top, mydb):
	submenu4.add_command(label=('Mask',), command=lambda : Query.wait('healthcare',1,mycursor, top, mydb))
	submenu4.add_separator()

	submenu4.add_command(label=('Sanitizer',), command=lambda : Query.wait('healthcare',2,mycursor, top, mydb))
	submenu4.add_separator()

	submenu4.add_command(label=('Disinfectant',), command=lambda : Query.wait('healthcare',3,mycursor, top, mydb))
	submenu4.add_separator()

	submenu4.add_command(label=('FaceShield',), command=lambda : Query.wait('healthcare',4,mycursor, top, mydb))
	submenu4.add_separator()

	submenu4.add_command(label=('Gloves',), command=lambda : Query.wait('healthcare',5,mycursor, top, mydb))
	submenu4.add_separator()

