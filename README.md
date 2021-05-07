ABOUT THE PROJECT :
  Customer will require to login to the system by providing his email id. Customer can search through the product catalogue and add the products to the cart. 
  The set of products added to the cart can be viewed and purchased by choosing the preferred mode of payment.

  Customer account login: 
    Customer logs into his account by entering his password. The entered id and password are compared against the values stored in the database table. If the values match, the user is able to log in. If the values do not match, an error message is displayed.
    The comparison operation is performed when the user clicks on “login” button. 
  Catalogue browsing:
    Products are listed in grid or list format. 
    Each product category has a submenu which contains all the items belonging to that category. When the user clicks on an item in the submenu,
    contents of “Category” table are fetched and displayed on the window. The price of the unit, quantity and brand of the selected item are displayed along with the product name as the user clicks on the product name. When the user clicks on the product name, all of its characteristic attributes are fetched from the respective database tables and displayed on the window. 
    The user can add the items to cart by clicking on the “add to cart” button, if he wishes to buy the product. On clicking the “add to cart” button,
    the product and its attributes are stored in a list and added into “cart” table. 
    The user can browse through the catalogue and add as many items as he wishes to buy into the cart.  At any time, the user can go to cart by clicking 
    on the “go to cart” button to finalise his order and make the payment. 
    The “go to cart” button directs the user to the cart window and displays the contents of the “cart” table in the database.

  Cart management:
    The products that the customer wishes to buy are added into the cart. In the cart, the user can specify the number of units of each item he wants to buy. 
    An entry box is used to accept the number of units from the user. The number is then multiplied with the price of the item. Total payment is computed by adding
    the product of price and number of units of all the items in the cart. 
    When the customer clicks on “confirm” button, the sum is computed and displayed on the window. The customer then clicks on “Payment” option to proceed further.
    “Payment” button directs the user to a new window where the mode of payment needs to be selected. 

  
