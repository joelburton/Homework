Homework: Telemarketer Script
=======

Introduction
--------
Our marketing department is running a new promotion this week for
all customers who have placed an order for over 20 Watermelons.
They want to make sure all eligible customers know about it, so
they've asked the Telemarketing Department to start placing calls.

In this folder is a python script called 'call.py' and two data files,
one containing the orders and another containing customer data.  Running
the 'call.py' script will output the next customer on the list to call.

The process the person making the calls has followed is:
* Run call.py
* Call the customer
* Open the customers.csv file in Excel and find the customer's row.
* Set today's date in the "called" column of the .csv file and save the file
* Repeat for the next customer on the list

Take a look at the script and get an idea of how it works.  What
are some issues you can think of running things this way?  How 
fast is it?  How much work needs to be done every time it runs?


Problem
--------
The system that generates the order data does not have access to 
the customer's telephone number, so we've been using this script
to make things easier, but there's still room for improvement.

We've run some tests and have found that it takes our telemarketer
on average about 24 seconds to search for the customer in the 
spreadsheet and update the "called" column.  Since the average
length of a call is 3 minutes, our performance consultant has 
indicated that our telemarketer could be calling an additional
133 people for every 1000 called.

How would you update this script so it not only displays the
next customer to call, but also updates the "called" column
in the 'customers.csv' file?  That way, every time the script 
is run it always shows a new customer to call.

