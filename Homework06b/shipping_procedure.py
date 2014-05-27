#!/usr/bin/env python
import robots
import sys

class Melon(object):

    def __init__(self, melon_type):
        self.melon_type = melon_type
        self.weight = 0.0
        self.color = None
        self.stickers = []

    def prep(self):
        robots.cleanerbot.clean(self)
        robots.stickerbot.apply_logo(self)
    
    def __str__(self):
        if self.weight <= 0:
            return self.melon_type
        else:
            return "%s %0.2fLB %s" % (self.color, self.weight, self.melon_type)
    

def main():
    f = open("standing_orders1.log")

    for line in f:
        (melon_type, quantity) = line.rstrip().split(':')
        quantity = int(quantity)
        
        count = 0
        melons = []
        while len(melons) < quantity:
            if count > 200:
                print "\nALL MELONS HAVE BEEN PICKED"
                print "ORDERS FAILED TO BE FULFILLED!"
                sys.exit()
            
            m = Melon(melon_type)
            robots.pickerbot.pick(m)
            count += 1
            
            m.prep()
            
            # evaluate melon
            presentable = robots.inspectorbot.evaluate(m)
            if presentable:
                melons.append(m)
            else:
                robots.trashbot.trash(m)
                continue

        print "------"
        print "Robots Picked %d %s for order of %d" % (count, melon_type, quantity)

        # Pack the melons for shipping
        boxes = robots.packerbot.pack(melons)
        # Ship the boxes
        robots.shipperbot.ship(boxes)
        print "------\n"


if __name__ == "__main__":
    main()
