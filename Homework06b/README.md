Introducing Winter Squashes
=======

TO DO
-------
- Finalize `robots.py` 

Email:
-------

```
To: jrdev48@ubermelon.co <Junior Developer #48>
From: mmelitopolski@ubermelon.co <Mel Melitopolski> 
Date: Fri June 13, 2014 5:03:20 PM PDT
Subject: Winter Squashes Are Coming

So I wanted to send a note out to give you a heads up about some 
big changes coming up.

Our CEO has decided to confront Squysh head on, and so we're going to
be introducing our new line of Winter Squash Watermelons in just 3 weeks.

Right now, our robotic production and delivery chain is handled by the code in
`shipping_procedure.py`.  It works great with our existing Melon classes- but can you check 
to see what we need to change in the `shipping_procedure.py` file so that it can handle Squash 
objects, in addition to Melon objects?

Also, our Uber Melon Winter Squashes have a very unique prep procedure. Our CEO has
decided it would be best to paint them before shipment. The issue is that currently,
the robots out in the factory are not painting the squashes with a watermelon 
color scheme since we never had to do that for watermelons, which already came in his
favorite color. 

So, please update the robot control script (which you'll find in `robots.py`) 
as needed so that it does paint the squashes correctly. To invoke the paint bot that's 
already been installed at the factory, you can call the following function:
    
    robots.PainterBot.watermelonize(melon)

Lastly, we anticipate a few more classes of specialty melons in the near future. Kobe Melons, 
Tanzanian Devil Squashes, Lobster Melons, and the ever popular Micro Musk Melon are just a few 
examples of what's possible.

So, please make sure the code can cleanly accommodate new products like these, without requiring us
to drastically modify the code too much each time we need to add a new product, and any distinct prep procedures
our new products might need.

Thanks for your help,
Mel
Team Lead
```

Attached:

1. [shipping_procedure.py](https://github.com/hackbrightacademy/Homework/blob/master/Homework06b/shipping_procedure.py)
1. [robots.py](https://github.com/hackbrightacademy/Homework/blob/master/Homework06b/robots.py)
