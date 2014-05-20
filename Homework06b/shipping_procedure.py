#!/usr/bin/env python
import robots

class Melon(object):
    def __init__(self, line):
        attrs = line.split()
        self.type = line[0]

    def prep(self):
        robots.CleanerBot.clean(self)
        robots.StickerBot.apply_logo(self)

def main():
    f = open("standing_orders.log")
    melons = []
    for line in f:
        m = Melon(line)
        # pick melon
        robots.PickerBot.pick(m)

        # evaluate melon
        presentable = robots.InspectorBot.evaluate(m)
        if not presentable:
            robots.Trashbot.trash(m)
            continue

        m.prep()

        # ship melon
        robots.ShipperBot.ship(m)

if __name__ == "__main__":
    main()
