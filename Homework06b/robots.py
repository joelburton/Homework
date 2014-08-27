import random

HEADER  = '\033[95m'
OK      = '\033[92m'
DANGER  = '\033[91m'
WARNING = '\033[93m'
ENDC    = '\033[0m'

class Robot(object):
    robot_name = 'Generic MelonBot'
    
    def display_status(self, msg):
        print "\033[93m[%s]\033[0m Status: %s" % (self.robot_name, msg), ENDC
    

class PickerBot(Robot):
    robot_name = 'PickerBot'
    
    def pick(self, melon):
        # Set characteristics of the melon that was picked
        weight = 10 * random.random()
        melon.weight = weight
        if melon.melon_type == 'Winter Squash':
            melon.color = 'Yellow'
        else:
            melon.color = 'Green'
        
        self.display_status("Picked a %s" % melon)

class CleanerBot(Robot):
    robot_name = 'CleanerBot'
    
    def clean(self, melon):
        self.display_status("Cleaned a %s" % melon)


class StickerBot(Robot):
    robot_name = "StickerBot"
    
    def apply_logo(self, melon):
        if random.random() < .9:
            melon.stickers.append('UberMelon Logo')
        if random.random() < .9:
            melon.stickers.append('Satisfaction Guaranteed')
        
        self.display_status("Applied logos to a %s" % melon)
    

class InspectorBot(Robot):
    robot_name = 'InspectorBot 2000'
    
    def evaluate(self, melon):
        self.display_status("Evaluating a %s" % melon)
        # Melons less than 3LB don't meet our quality standards
        if melon.weight < 3:
            self.display_status(DANGER + "%s weight less than 3lbs!  REJECTED!!" % melon)
            return False
        
        # Melons over 8LB cost too much to ship!
        if melon.weight > 8:
            self.display_status(DANGER + "%s weight over 8lbs!  REJECTED!!" % melon)
            return False

        # Melons should have two stickers applied
        if len(melon.stickers) < 2:
            self.display_status(DANGER + "%s is not labeled correctly!  REJECTED!!" % melon)
            return False

        # All melons should be green!
        if melon.color != 'Green':
            self.display_status(DANGER + "%s is not Green!  All melons must be Green!  REJECTED!!" % melon)
            return False
        
        self.display_status(OK + "%s Passes" % melon)
        return True
    

class PackerBot(Robot):
    robot_name = 'PackerBot'
    
    def pack(self, melons):
        box = Box()
        boxes = [box]
        
        for melon in melons:
            self.display_status("Packing %s" % melon)
            # If the current box is over the limit, get a new box
            if box.at_limit():
                box = Box()
                boxes.append(box)
            
            box.add_to_box(melon)
        
        return boxes
    

class ShipperBot(Robot):
    robot_name = 'ShipperBot'
    
    def ship(self, boxes):
        self.display_status("Shipping %s boxes of melons." % len(boxes))
        for i in range(len(boxes)):
            self.display_status("Box %d Weight: %0.2flbs" % (i+1, boxes[i].weight() ))


class TrashBot(Robot):
    robot_name = 'TrashBot'
    
    def trash(self, melon):
        self.display_status("Sending %s to the compost" % melon)


class PainterBot(Robot):
    robot_name = 'PainterBot'
    
    def paint(self, melon):
        self.display_status("Painting %s Green" % melon)
        melon.color = 'Green'
    


class Box(object):
    max_melons = 5
    
    def __init__(self):
        self.contents = []
    
    def at_limit(self):
        return len(self.contents) >= self.max_melons
    
    def add_to_box(self, melon):
        if self.at_limit():
            print "Box is full! Dropped melon on the floor!"
            return False

        self.contents.append(melon)
        return True
    
    def weight(self):
        weight = 0.0
        for item in self.contents:
            weight += item.weight
        
        return weight
    

    def display_contents(self):
        str = "|"
        for m in self.contents:
            str += " %s |" % m

        return str
    
    def __str__(self):
        return "Box contains: ", self.display_contents()


# Instantiate some Robots
random.seed()
pickerbot    = PickerBot()
cleanerbot   = CleanerBot()
stickerbot   = StickerBot()
inspectorbot = InspectorBot()
trashbot     = TrashBot()
packerbot    = PackerBot()
shipperbot   = ShipperBot()
painterbot   = PainterBot()