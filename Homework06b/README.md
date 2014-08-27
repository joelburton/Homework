
Introducing Winter Squashes
=======

Email:
-------

```
To: jrdev48@ubermelon.co <Junior Developer #48>
From: mmelitopolski@ubermelon.co <Mel Melitopolski> 
Date: Fri June 13, 2014 5:03:20 PM PDT
Subject: Winter Squashes Are Coming

So I wanted to send a note out to give you a heads up about some big changes coming up!

Our CEO has decided to confront Squysh head on, and so we're going to
be introducing our new line of Uber Melon Winter Squashes in just 10 days.

As you know, our CEO has invested billions of VC money in our robotic production
and order fullfillment delivery chain.  It's all managed by the code in 
"shipping_procedure.py".  It works great with melons (e.g. when processing
the "standing_orders1.log" file)- but can you check to see what we need to change 
so that it can handle Squashes, in addition to Melons?  The file "standing_orders2.log"
has an order for squashes.

Before shipping, all melons are evaulated by the InspectorBot for quality standards.
The Winter Squashes are being rejected because they are not green like the watermelons
are.  We've contacted the company that made the InspectorBot, but they've informed us
it will cost millions of dollars in consulting fees to upgrade the robot's software
to handle two types of melons.  As a result, the CEO has decided it would be
best to paint the Winter Squash green with black stripes to match the watermelons.

So, please update the robot control script (which you'll find in `shipping_procedure.py`)
to add a Squash melon class that has the special prep procedure to paint the
squashes correctly.  To invoke the paint bot that's already been installed at the 
factory, you can call the following function:
    
    robots.painterbot.paint(self)


Thanks for your help,
Mel
Team Lead

P.S. Remember, any changes to the robot control script ("robots.py") would 
cost us hundreds of millions in contract fees to get implemented, so I'm hoping you can
do this without changing that file at all!
```

Attached:

1. [shipping_procedure.py](https://github.com/hackbrightacademy/Homework/blob/master/Homework06b/shipping_procedure.py)
1. [robots.py](https://github.com/hackbrightacademy/Homework/blob/master/Homework06b/robots.py)
1. [standing_orders1.log](https://github.com/hackbrightacademy/Homework/blob/master/Homework06b/standing_orders1.log)
1. [standing_orders2.log](https://github.com/hackbrightacademy/Homework/blob/master/Homework06b/standing_orders2.log)
