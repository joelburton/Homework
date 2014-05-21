files:
  customers.csv - list of all customers with email & phone number
  orders.csv - list of all orders places last week
  call.py - python script that finds next customers to call who has placed an order for a specific melon type (e.g. watermelon)


Call Center at ubermelon
I run my program that tells me the next person to call to tell about our new wintersquash promotion
Run the program and it outputs a name and phone number
  * program reads our orders to find customers who ordered watermelons (orders has customer id but no phone number) orders come from another program that does not have access to the phone number.  Use email address as key

  * then the program reads in the customers.csv to find their phone number to find the next person who has not been called


Up until now, the sales person opens the .csv file in excel and sets the "called" column to today's date.  Update the program so it automatically sets the current date when they run the program to (indicate that they have called the customer) instead of having to open the customers.csv file in excel in order to.   Every time they run they can the next customer.

